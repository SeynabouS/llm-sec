# =============================================================================
# LLM Cybersecurity Course — Simplified Makefile
# Author: Badr TAJINI — ECE 2025/2026
# 
# STRUCTURE: All labs under labs/ and project under project/
# VENV: Single root .venv for entire course
# =============================================================================

.PHONY: help venv install clean test all \
        lab1-tests lab2-tests lab3-tests lab4-tests project-tests \
        w01-day w02-day w03-day w04-day project-test

# -----------------------------------------------------------------------------
# Paths (simplified!)
# -----------------------------------------------------------------------------
LAB1_DIR := labs/lab1
LAB2_DIR := labs/lab2
LAB3_DIR := labs/lab3
LAB4_DIR := labs/lab4
PROJECT_DIR := project

# Single root venv
VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

# Fallback to system Python if venv doesn't exist
SYSTEM_PYTHON := $(shell command -v python3 2>/dev/null || command -v python 2>/dev/null)

# -----------------------------------------------------------------------------
# Default target
# -----------------------------------------------------------------------------
help: ## Show this help message
	@echo "LLM Cybersecurity Course — Make Targets"
	@echo "========================================"
	@echo ""
	@echo "Setup:"
	@echo "  make venv      Create root virtual environment"
	@echo "  make install   Install all dependencies"
	@echo "  make clean     Remove venv and caches"
	@echo ""
	@echo "Daily Workflows:"
	@echo "  make w01-day       Lab 1 tests + reminders"
	@echo "  make w02-day       Lab 2 tests + reminders"
	@echo "  make w03-day       Lab 3 tests + reminders"
	@echo "  make w04-day       Lab 4 tests + reminders"
	@echo "  make project-test  Final project tests + reminders"
	@echo ""
	@echo "Tests:"
	@echo "  make test      Run all tests"
	@echo "  make lab1-tests"
	@echo "  make lab2-tests"
	@echo "  make lab3-tests"
	@echo "  make lab4-tests"
	@echo "  make project-tests"
	@echo ""

# -----------------------------------------------------------------------------
# Setup
# -----------------------------------------------------------------------------
venv: ## Create root virtual environment
	@echo "Creating virtual environment at $(VENV)..."
	@$(SYSTEM_PYTHON) -m venv $(VENV)
	@echo "Done! Activate with: source $(VENV)/bin/activate"

install: venv ## Install all dependencies
	@echo "Installing dependencies from requirements.txt..."
	@$(PIP) install --upgrade pip
	@$(PIP) install -r requirements.txt
	@echo "Done! All labs ready to use."

clean: ## Remove venv and caches
	@echo "Cleaning up..."
	@rm -rf $(VENV)
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	@echo "Done!"

# -----------------------------------------------------------------------------
# Test Runners
# -----------------------------------------------------------------------------
test: lab1-tests lab2-tests lab3-tests lab4-tests project-tests ## Run all tests
	@echo "All tests complete!"

lab1-tests: ## Run Lab 1 tests
	@echo "== Lab 1 Tests =="
	@if [ -x "$(PYTHON)" ]; then \
		PYTHONPATH=$(LAB1_DIR) $(PYTHON) -m unittest discover -s $(LAB1_DIR)/tests -v; \
	else \
		PYTHONPATH=$(LAB1_DIR) $(SYSTEM_PYTHON) -m unittest discover -s $(LAB1_DIR)/tests -v; \
	fi

lab2-tests: ## Run Lab 2 tests
	@echo "== Lab 2 Tests =="
	@if [ -x "$(PYTHON)" ]; then \
		PYTHONPATH=$(LAB2_DIR) $(PYTHON) -m unittest discover -s $(LAB2_DIR)/tests -v; \
	else \
		PYTHONPATH=$(LAB2_DIR) $(SYSTEM_PYTHON) -m unittest discover -s $(LAB2_DIR)/tests -v; \
	fi

lab3-tests: ## Run Lab 3 tests
	@echo "== Lab 3 Tests =="
	@if [ -x "$(PYTHON)" ]; then \
		PYTHONPATH=$(LAB3_DIR) $(PYTHON) -m unittest discover -s $(LAB3_DIR)/tests -v; \
	else \
		PYTHONPATH=$(LAB3_DIR) $(SYSTEM_PYTHON) -m unittest discover -s $(LAB3_DIR)/tests -v; \
	fi

lab4-tests: ## Run Lab 4 tests
	@echo "== Lab 4 Tests =="
	@if [ -x "$(PYTHON)" ]; then \
		PYTHONPATH=$(LAB4_DIR) $(PYTHON) -m unittest discover -s $(LAB4_DIR)/tests -v; \
	else \
		PYTHONPATH=$(LAB4_DIR) $(SYSTEM_PYTHON) -m unittest discover -s $(LAB4_DIR)/tests -v; \
	fi

project-tests: ## Run Final Project tests
	@echo "== Final Project Tests =="
	@if [ -x "$(PYTHON)" ]; then \
		PYTHONPATH=$(PROJECT_DIR) GEMINI_API_KEY=dummy MODEL_ID=gemini-2.5-flash \
		$(PYTHON) -m unittest discover -s $(PROJECT_DIR)/tests -v; \
	else \
		PYTHONPATH=$(PROJECT_DIR) GEMINI_API_KEY=dummy MODEL_ID=gemini-2.5-flash \
		$(SYSTEM_PYTHON) -m unittest discover -s $(PROJECT_DIR)/tests -v; \
	fi

# -----------------------------------------------------------------------------
# Daily Workflows (with reminders)
# -----------------------------------------------------------------------------
w01-day: lab1-tests ## Lab 1 daily workflow
	@echo ""
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "Lab 1 Key Commands:"
	@echo "  cd $(LAB1_DIR)"
	@echo "  python -m src.app                    # Run analyzer"
	@echo "  cat reports/baseline.json            # Check output"
	@echo ""
	@echo "Deliverables: reports/baseline.json (JSON valid, OWASP findings)"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

w02-day: lab2-tests ## Lab 2 daily workflow
	@echo ""
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "Lab 2 Key Commands:"
	@echo "  cd $(LAB2_DIR)"
	@echo "  npx promptfoo eval -c promptfooconfig.yaml"
	@echo "  python tools/metrics.py reports/results.json reports/metrics.csv"
	@echo ""
	@echo "Deliverables: prompts/*.txt, reports/metrics.csv"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

w03-day: lab3-tests ## Lab 3 daily workflow
	@echo ""
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "Lab 3 Key Commands:"
	@echo "  cd $(LAB3_DIR)"
	@echo "  semgrep --config=auto src/           # Run Semgrep"
	@echo "  checkov -d data/                     # Run Checkov"
	@echo ""
	@echo "Deliverables: reports/semgrep_results.json, reports/checkov_results.json"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

w04-day: lab4-tests ## Lab 4 daily workflow
	@echo ""
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "Lab 4 Key Commands:"
	@echo "  cd $(LAB4_DIR)"
	@echo "  python -m src.classifier             # Run classifier"
	@echo "  python tools/analyze.py              # Generate metrics"
	@echo ""
	@echo "Deliverables: reports/classification_results.json, reports/metrics.csv"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

project-test: project-tests ## Final Project daily workflow
	@echo ""
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "Final Project Key Commands:"
	@echo "  cd $(PROJECT_DIR)"
	@echo "  npx promptfoo eval -c promptfooconfig.yaml"
	@echo "  python tools/metrics.py reports/results.json reports/metrics.csv"
	@echo ""
	@echo "Targets: JSON≥0.95, Safety≥0.85, Citations≥0.80"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# -----------------------------------------------------------------------------
# All daily workflows
# -----------------------------------------------------------------------------
all: w01-day w02-day w03-day w04-day project-test ## Run all daily workflows
	@echo ""
	@echo "✅ All labs and project tested!"
