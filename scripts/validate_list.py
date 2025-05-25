#!/usr/bin/env python3
"""
Validation script for the Awesome Free Land Parcel Data list.
Checks for duplicates, proper formatting, and organization.
"""

import re
import sys
from urllib.parse import urlparse
from collections import defaultdict


def extract_links_from_markdown(content):
    """Extract all markdown links from content."""
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    return re.findall(pattern, content)


def check_duplicates(links):
    """Check for duplicate URLs and names."""
    urls = defaultdict(list)
    names = defaultdict(list)
    
    for name, url in links:
        urls[url].append(name)
        names[name.lower()].append(url)
    
    duplicates = []
    
    # Check for duplicate URLs
    for url, name_list in urls.items():
        if len(name_list) > 1:
            duplicates.append(f"Duplicate URL: {url} used for: {', '.join(name_list)}")
    
    # Check for duplicate names (case-insensitive)
    for name, url_list in names.items():
        if len(url_list) > 1:
            duplicates.append(f"Duplicate name: {name} used for: {', '.join(url_list)}")
    
    return duplicates


def check_https_usage(links):
    """Check if HTTPS is used where possible."""
    http_links = []
    
    for name, url in links:
        parsed = urlparse(url)
        if parsed.scheme == 'http' and parsed.netloc not in ['localhost', '127.0.0.1']:
            http_links.append(f"{name}: {url}")
    
    return http_links


def check_alphabetical_order(content):
    """Check if entries within sections are alphabetically ordered."""
    sections = re.split(r'^##\s+(.+)$', content, flags=re.MULTILINE)
    issues = []
    
    for i in range(1, len(sections), 2):
        section_name = sections[i]
        section_content = sections[i + 1] if i + 1 < len(sections) else ""
        
        # Skip certain sections that don't need alphabetical ordering
        skip_sections = ['Contents', 'Contributing', 'License']
        if section_name in skip_sections:
            continue
        
        # Check if this section has subsections (### headers)
        if re.search(r'^###\s+', section_content, re.MULTILINE):
            # This section has subsections, check each subsection separately
            subsections = re.split(r'^(###\s+.+)$', section_content, flags=re.MULTILINE)
            for j in range(1, len(subsections), 2):
                subsection_name = subsections[j].strip()
                subsection_content = subsections[j + 1] if j + 1 < len(subsections) else ""
                
                # Extract list items from subsection
                list_items = re.findall(r'^- \[([^\]]+)\]', subsection_content, re.MULTILINE)
                
                if len(list_items) > 1:
                    sorted_items = sorted(list_items, key=str.lower)
                    if list_items != sorted_items:
                        issues.append(f"Subsection '{subsection_name}' in '{section_name}' is not alphabetically ordered")
        else:
            # No subsections, check the section directly
            list_items = re.findall(r'^- \[([^\]]+)\]', section_content, re.MULTILINE)
            
            if len(list_items) > 1:
                sorted_items = sorted(list_items, key=str.lower)
                if list_items != sorted_items:
                    issues.append(f"Section '{section_name}' is not alphabetically ordered")
    
    return issues


def check_description_length(links):
    """Check if descriptions are reasonable length."""
    long_descriptions = []
    
    for name, url in links:
        # Find the description part (after the link)
        # This is a simplified check - in practice, you'd need to parse the full line
        if len(name) > 100:
            long_descriptions.append(f"{name}: Name too long ({len(name)} chars)")
    
    return long_descriptions


def validate_awesome_list(filename):
    """Main validation function."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
        return False
    
    print(f"Validating {filename}...")
    
    # Extract all links
    links = extract_links_from_markdown(content)
    print(f"Found {len(links)} links")
    
    issues = []
    
    # Check for required elements
    if '[![Awesome](https://awesome.re/badge.svg)]' not in content:
        issues.append("Missing awesome badge")
    
    if '## Contents' not in content:
        issues.append("Missing table of contents")
    
    if '## Contributing' not in content:
        issues.append("Missing contributing section")
    
    # Check for duplicates
    duplicates = check_duplicates(links)
    issues.extend(duplicates)
    
    # Check HTTPS usage
    http_links = check_https_usage(links)
    if http_links:
        issues.append("HTTP links found (consider HTTPS):")
        issues.extend(f"  - {link}" for link in http_links)
    
    # Check alphabetical order
    order_issues = check_alphabetical_order(content)
    issues.extend(order_issues)
    
    # Check description length
    length_issues = check_description_length(links)
    issues.extend(length_issues)
    
    # Report results
    if issues:
        print("\nIssues found:")
        for issue in issues:
            print(f"  - {issue}")
        return False
    else:
        print("✅ All checks passed!")
        return True


if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "README.md"
    success = validate_awesome_list(filename)
    sys.exit(0 if success else 1) 