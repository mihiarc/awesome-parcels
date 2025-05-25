# Project Documentation

## Overview

This repository contains a curated list of free land parcel data sources, tools, and resources. It follows the [awesome list](https://awesome.re) format and standards.

## Repository Structure

```
awesome-parcels/
├── README.md                    # Main awesome list
├── CONTRIBUTING.md              # Contribution guidelines
├── PROJECT.md                   # This file - project documentation
├── Makefile                     # Development tasks
├── requirements.txt             # Python dependencies
├── .github/                     # GitHub-specific files
│   ├── workflows/
│   │   └── awesome-lint.yml     # CI/CD pipeline
│   ├── ISSUE_TEMPLATE/
│   │   ├── add-resource.md      # Template for adding resources
│   │   └── bug-report.md        # Template for reporting issues
│   ├── pull_request_template.md # PR template
│   ├── markdown-link-check.json # Link checker configuration
│   └── markdownlint.json        # Markdown linter configuration
└── scripts/
    └── validate_list.py         # Validation script
```

## Content Organization

### Geographic Hierarchy

The list is organized geographically in the following order:

1. **Global Sources** - Worldwide datasets
2. **United States** - Organized by administrative level:
   - Federal (national agencies)
   - State Level (state governments)
   - County/Local (local governments)
3. **Other Countries** - Organized by continent/region:
   - Canada
   - Europe
   - Australia & New Zealand
   - Other Countries

### Functional Categories

After geographic sources, the list includes:

- **Tools & Libraries** - Software for working with parcel data
- **APIs** - Programmatic access to data
- **Visualization Tools** - Tools for displaying and analyzing data
- **Data Processing** - Tools for transforming and managing data
- **Educational Resources** - Learning materials
- **Standards & Formats** - Technical specifications

## Quality Standards

### Data Sources

All data sources must meet these criteria:

- **Free Access**: No payment required for basic access
- **Legal**: Legally accessible and redistributable
- **Quality**: Reliable and accurate data
- **Maintained**: Actively maintained or recently updated
- **Documented**: Clear documentation or metadata available

### Tools and Resources

- **Open Source**: Preferably open-source (exceptions for high-quality free tools)
- **Active Development**: Should be actively maintained
- **Relevant**: Must be specifically useful for land parcel data
- **Well-Documented**: Should have comprehensive documentation

## Maintenance Workflow

### Adding New Resources

1. **Research**: Verify the resource meets quality standards
2. **Categorization**: Determine the appropriate section
3. **Formatting**: Follow the established format
4. **Validation**: Run validation scripts
5. **Submission**: Create a pull request with proper documentation

### Regular Maintenance

- **Monthly**: Check for broken links
- **Quarterly**: Review and update descriptions
- **Annually**: Comprehensive review of all resources

### Automated Checks

The repository includes automated checks for:

- Link validity
- Markdown formatting
- Awesome list format compliance
- Alphabetical ordering within sections

## Development Setup

### Prerequisites

- Python 3.7+
- Node.js (for markdown tools)
- Git

### Setup Commands

```bash
# Clone the repository
git clone https://github.com/mihiarc/awesome-parcels.git
cd awesome-parcels

# Set up development environment
make dev-setup

# Run validation
make check
```

### Available Make Commands

- `make help` - Show available commands
- `make validate` - Run Python validation script
- `make format` - Check markdown formatting
- `make check-links` - Check for broken links
- `make check` - Run all validation checks
- `make stats` - Show list statistics
- `make clean` - Clean temporary files

## Validation Script

The `scripts/validate_list.py` script checks for:

- Required awesome list elements (badge, TOC, contributing section)
- Duplicate URLs and resource names
- HTTPS usage where possible
- Alphabetical ordering within sections
- Description length guidelines

## GitHub Integration

### Issue Templates

- **Add Resource**: Structured template for suggesting new resources
- **Bug Report**: Template for reporting problems with existing resources

### Pull Request Template

Ensures contributors provide necessary information and follow quality standards.

### GitHub Actions

Automated workflow that runs on every push and pull request:

- Format validation
- Link checking
- Awesome list compliance

## Best Practices

### For Maintainers

1. **Review Thoroughly**: Check each submission against quality standards
2. **Test Links**: Verify all links work and point to correct resources
3. **Maintain Consistency**: Ensure formatting and style consistency
4. **Document Changes**: Use clear commit messages and PR descriptions
5. **Engage Community**: Respond promptly to issues and PRs

### For Contributors

1. **Read Guidelines**: Review CONTRIBUTING.md before submitting
2. **Check Existing Content**: Avoid duplicates
3. **Follow Format**: Use the established format exactly
4. **Provide Context**: Include clear descriptions in PRs
5. **Test Your Changes**: Run validation scripts before submitting

## Future Enhancements

Potential improvements to consider:

- **Automated Link Checking**: More sophisticated link validation
- **Data Quality Metrics**: Scoring system for data sources
- **Geographic Coverage Maps**: Visual representation of coverage
- **API Integration**: Automated metadata collection
- **Community Ratings**: User feedback system

## License

This project is released under the CC0 1.0 Universal license, placing it in the public domain. See the README for full license details.

## Contact

For questions about the project structure or maintenance, please:

1. Check existing issues and discussions
2. Open a new issue with the "question" label
3. Follow the project's code of conduct

---

*This documentation is maintained alongside the awesome list and should be updated when significant changes are made to the project structure or processes.* 