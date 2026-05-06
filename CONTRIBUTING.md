# Contributing

Thank you for your interest in contributing to this project!

## Getting Started

1. Fork the repository
2. Clone your fork
3. Create a virtual environment: `python -m venv venv`
4. Activate it: `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
5. Install dependencies: `pip install -e ".[dev]"`

## Code Style

- Format with Black: `black src/ tests/`
- Sort imports with isort: `isort src/ tests/`
- Lint with flake8: `flake8 src/ tests/`

## Running Tests

```bash
pytest
pytest --cov=src  # with coverage report
