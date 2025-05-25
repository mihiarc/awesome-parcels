.PHONY: help validate format check-links install clean

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

validate: ## Validate the awesome list format and content
	@echo "Running validation script..."
	@python3 scripts/validate_list.py README.md

sort: ## Sort entries within sections alphabetically
	@echo "Sorting sections..."
	@python3 scripts/sort_sections.py README.md

format: ## Check markdown formatting
	@echo "Checking markdown format..."
	@if command -v markdownlint >/dev/null 2>&1; then \
		markdownlint README.md CONTRIBUTING.md; \
	else \
		echo "markdownlint not installed. Install with: npm install -g markdownlint-cli"; \
	fi

check-links: ## Check for broken links
	@echo "Checking links..."
	@if command -v markdown-link-check >/dev/null 2>&1; then \
		markdown-link-check README.md; \
	else \
		echo "markdown-link-check not installed. Install with: npm install -g markdown-link-check"; \
	fi

install: ## Install development dependencies
	@echo "Installing Python dependencies..."
	@pip3 install -r requirements.txt
	@echo "Installing Node.js dependencies..."
	@if command -v npm >/dev/null 2>&1; then \
		npm install -g markdownlint-cli markdown-link-check; \
	else \
		echo "npm not found. Please install Node.js to use markdown tools."; \
	fi

check: validate format ## Run all checks

clean: ## Clean up temporary files
	@echo "Cleaning up..."
	@find . -name "*.pyc" -delete
	@find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
	@echo "Clean complete."

# Development helpers
dev-setup: install ## Set up development environment
	@echo "Development environment setup complete!"
	@echo "Run 'make check' to validate the awesome list."

stats: ## Show statistics about the list
	@echo "Awesome List Statistics:"
	@echo "======================="
	@echo "Total lines: $$(wc -l < README.md)"
	@echo "Total links: $$(grep -o '\[.*\](.*' README.md | wc -l)"
	@echo "Sections: $$(grep -c '^## ' README.md)"
	@echo "Subsections: $$(grep -c '^### ' README.md)" 