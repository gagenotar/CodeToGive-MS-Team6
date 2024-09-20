# Define environment variables
ENV_FILE = .env

# Define the main file to run the FastAPI app
APP_FILE = main

# Define the name of your virtual environment
VENV = venv

# Define Python binary from the virtual environment
PYTHON = $(VENV)/bin/python

# Define pip binary from the virtual environment
PIP = $(VENV)/bin/pip

# Define the default port for FastAPI to run on
PORT = 8000

# Create virtual environment
.PHONY: venv
venv:
	python3 -m venv $(VENV)

# Install dependencies from requirements.txt
.PHONY: install
install: venv
	$(PIP) install -r requirements.txt

# Run FastAPI using uvicorn
.PHONY: run
run: install
	$(PYTHON) -m uvicorn $(APP_FILE):app --reload --port $(PORT)

# Run FastAPI on a custom port
.PHONY: run-custom-port
run-custom-port:
	$(PYTHON) -m uvicorn $(APP_FILE):app --reload --port $(PORT)

# Lint code using flake8
.PHONY: lint
lint:
	$(PIP) install flake8
	$(VENV)/bin/flake8 $(APP_FILE)

# Clean up the environment
.PHONY: clean
clean:
	rm -rf $(VENV)
	rm -rf __pycache__

# Run database migrations (example for Alembic, modify as needed)
.PHONY: migrate
migrate:
	alembic upgrade head

# Example of running tests
.PHONY: test
test:
	$(PYTHON) -m pytest

# Source the .env file and export the environment variables
.PHONY: load-env
load-env:
	export $(shell sed 's/=.*//' $(ENV_FILE))

# Load the .env file and run FastAPI
.PHONY: run-with-env
run-with-env: load-env run
