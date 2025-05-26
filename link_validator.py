#!/usr/bin/env python3
"""
Link Validator for Awesome Parcels README.md
Validates all URLs in the README.md file and reports their status.
"""

import re
import requests
import time
from urllib.parse import urlparse
from typing import List, Tuple, Dict
import sys

def extract_urls_from_markdown(file_path: str) -> List[str]:
    """Extract all URLs from a markdown file."""
    urls = []
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Pattern to match markdown links [text](url)
    markdown_link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    matches = re.findall(markdown_link_pattern, content)
    
    for text, url in matches:
        # Skip anchor links and relative links
        if not url.startswith('#') and not url.startswith('./') and not url.startswith('../'):
            urls.append(url.strip())
    
    # Also find bare URLs (http/https)
    bare_url_pattern = r'https?://[^\s\)]+(?=\s|\)|$)'
    bare_urls = re.findall(bare_url_pattern, content)
    urls.extend(bare_urls)
    
    # Remove duplicates while preserving order
    seen = set()
    unique_urls = []
    for url in urls:
        if url not in seen:
            seen.add(url)
            unique_urls.append(url)
    
    return unique_urls

def validate_url(url: str, timeout: int = 10) -> Tuple[str, int, str]:
    """
    Validate a single URL and return status information.
    Returns: (url, status_code, status_message)
    """
    try:
        # Add user agent to avoid blocking
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.head(url, timeout=timeout, headers=headers, allow_redirects=True)
        
        # If HEAD request fails, try GET
        if response.status_code >= 400:
            response = requests.get(url, timeout=timeout, headers=headers, allow_redirects=True)
        
        return url, response.status_code, "OK" if response.status_code < 400 else "Error"
    
    except requests.exceptions.Timeout:
        return url, 0, "Timeout"
    except requests.exceptions.ConnectionError:
        return url, 0, "Connection Error"
    except requests.exceptions.RequestException as e:
        return url, 0, f"Request Error: {str(e)}"
    except Exception as e:
        return url, 0, f"Unknown Error: {str(e)}"

def categorize_urls(urls: List[str]) -> Dict[str, List[str]]:
    """Categorize URLs by domain/organization for better reporting."""
    categories = {}
    
    for url in urls:
        try:
            domain = urlparse(url).netloc.lower()
            
            # Group by main domain
            if 'maine.gov' in domain:
                category = 'Maine Government'
            elif 'data.gov' in domain:
                category = 'Data.gov'
            elif 'github.com' in domain:
                category = 'GitHub'
            elif 'arcgis.com' in domain or 'esri.com' in domain:
                category = 'ArcGIS/Esri'
            elif any(state in domain for state in ['utah.gov', 'texas.gov', 'oregon.gov', 'virginia.gov']):
                category = 'State Government'
            elif 'census.gov' in domain:
                category = 'US Census'
            elif any(fed in domain for fed in ['usgs.gov', 'blm.gov', 'usda.gov']):
                category = 'Federal Government'
            else:
                category = 'Other'
            
            if category not in categories:
                categories[category] = []
            categories[category].append(url)
        except:
            if 'Other' not in categories:
                categories['Other'] = []
            categories['Other'].append(url)
    
    return categories

def main():
    """Main function to validate all links in README.md."""
    print("🔗 Awesome Parcels Link Validator")
    print("=" * 50)
    
    # Extract URLs from README.md
    try:
        urls = extract_urls_from_markdown('README.md')
        print(f"Found {len(urls)} unique URLs to validate\n")
    except FileNotFoundError:
        print("❌ README.md file not found!")
        sys.exit(1)
    
    # Categorize URLs
    categories = categorize_urls(urls)
    
    # Validate URLs
    results = []
    failed_urls = []
    
    print("🔍 Validating URLs...")
    print("-" * 30)
    
    for i, url in enumerate(urls, 1):
        print(f"[{i}/{len(urls)}] Checking: {url[:60]}{'...' if len(url) > 60 else ''}")
        
        url_result, status_code, status_message = validate_url(url)
        results.append((url_result, status_code, status_message))
        
        if status_code == 0 or status_code >= 400:
            failed_urls.append((url_result, status_code, status_message))
            print(f"    ❌ {status_code} - {status_message}")
        else:
            print(f"    ✅ {status_code} - {status_message}")
        
        # Small delay to be respectful to servers
        time.sleep(0.5)
    
    # Summary Report
    print("\n" + "=" * 50)
    print("📊 VALIDATION SUMMARY")
    print("=" * 50)
    
    total_urls = len(urls)
    successful_urls = total_urls - len(failed_urls)
    success_rate = (successful_urls / total_urls) * 100 if total_urls > 0 else 0
    
    print(f"Total URLs checked: {total_urls}")
    print(f"Successful: {successful_urls} ({success_rate:.1f}%)")
    print(f"Failed: {len(failed_urls)} ({100-success_rate:.1f}%)")
    
    # Category breakdown
    print(f"\n📂 URLs by Category:")
    for category, category_urls in categories.items():
        print(f"  {category}: {len(category_urls)} URLs")
    
    # Failed URLs Report
    if failed_urls:
        print(f"\n❌ FAILED URLs ({len(failed_urls)}):")
        print("-" * 30)
        for url, status_code, status_message in failed_urls:
            print(f"• {url}")
            print(f"  Status: {status_code} - {status_message}\n")
    else:
        print(f"\n🎉 All URLs are working correctly!")
    
    # Save detailed report
    with open('link_validation_report.txt', 'w', encoding='utf-8') as f:
        f.write("Awesome Parcels Link Validation Report\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total URLs: {total_urls}\n")
        f.write(f"Success Rate: {success_rate:.1f}%\n\n")
        
        f.write("DETAILED RESULTS:\n")
        f.write("-" * 20 + "\n")
        for url, status_code, status_message in results:
            status_icon = "✅" if status_code > 0 and status_code < 400 else "❌"
            f.write(f"{status_icon} [{status_code}] {url} - {status_message}\n")
        
        if failed_urls:
            f.write(f"\nFAILED URLs ({len(failed_urls)}):\n")
            f.write("-" * 20 + "\n")
            for url, status_code, status_message in failed_urls:
                f.write(f"• {url}\n")
                f.write(f"  Status: {status_code} - {status_message}\n\n")
    
    print(f"\n📄 Detailed report saved to: link_validation_report.txt")
    
    return len(failed_urls) == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 