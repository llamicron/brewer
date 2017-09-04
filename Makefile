build:
	python setup.py sdist

upload:
	python setup.py sdist uploa

clean:
	rm -rf dist/
	rm -rf htmlcov/


