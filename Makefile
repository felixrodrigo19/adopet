.ONESHELL:

.PHONY: clean install run all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -iname '__pycache__' -delete
	find . -type f -name '*.log' -delete

install:
	python -m venv venv; \
	venv/bin/activate; \
	pip install -e .['dev'];

run:
	venv/bin/activate; \
	export FLASK_DEBUG=true && \
	export FLASK_APP=adopet/app.py && \
	flask run

all: clean install run