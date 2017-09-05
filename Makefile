.PHONY: docs

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

