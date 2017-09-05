.PHONY: docs

install:
	python setup.py sdist

build:
	python setup.py sdist

upload:
	twine upload dist/*

clean:
	rm -rf dist/
	rm -rf htmlcov/

docs:
	$(MAKE) -C docs html
	$(MAKE) -C docs server

test:
	pytest --cov-report html --cov=brewer/  tests/
