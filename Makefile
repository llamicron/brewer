.PHONY: docs

install: build
	pip install dist/*

build:
	python setup.py sdist

upload: build
	twine upload dist/*

clean:
	rm -rf dist/
	rm -rf htmlcov/

test:
	pytest tests/

docs: build install
	pdoc --html --html-dir=docs/ brewer
