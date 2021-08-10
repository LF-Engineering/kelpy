.PHONY: setup

setup:
	python3 -m venv .venv
	./.venv/bin/pip install -e .
	./.venv/bin/pip install -r requirements-dev.txt

functional-tests:
	behave
