#!/usr/bin/env python3
"""
Script to sort entries within sections alphabetically.
"""

import re
import sys


def sort_markdown_sections(content):
    """Sort entries within each section alphabetically."""
    
    # Split content by sections (## headers)
    sections = re.split(r'^(##\s+.+)$', content, flags=re.MULTILINE)
    
    result = []
    
    for i, section in enumerate(sections):
        if i == 0:
            # Content before first section
            result.append(section)
        elif section.startswith('##'):
            # Section header
            result.append(section)
        else:
            # Section content
            result.append(sort_section_content(section))
    
    return ''.join(result)


def sort_section_content(content):
    """Sort the content of a single section."""
    lines = content.split('\n')
    result_lines = []
    current_list = []
    in_list = False
    
    for line in lines:
        if line.strip().startswith('- ['):
            # This is a list item
            if not in_list:
                in_list = True
            current_list.append(line)
        else:
            # Not a list item
            if in_list and current_list:
                # Sort the accumulated list items
                sorted_list = sort_list_items(current_list)
                result_lines.extend(sorted_list)
                current_list = []
                in_list = False
            result_lines.append(line)
    
    # Handle any remaining list items
    if current_list:
        sorted_list = sort_list_items(current_list)
        result_lines.extend(sorted_list)
    
    return '\n'.join(result_lines)


def sort_list_items(items):
    """Sort a list of markdown list items alphabetically by the link text."""
    def extract_link_text(item):
        # Extract the text between [ and ]
        match = re.search(r'\[([^\]]+)\]', item)
        if match:
            return match.group(1).lower()
        return item.lower()
    
    return sorted(items, key=extract_link_text)


def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else "README.md"
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
        return 1
    
    sorted_content = sort_markdown_sections(content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(sorted_content)
    
    print(f"Sorted sections in {filename}")
    return 0


if __name__ == "__main__":
    sys.exit(main()) 