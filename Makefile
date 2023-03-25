PYTHON ?= python3
PYPIRC_CONFIG ?= $(HOME)/.pypirc
PYPI_REPO_NAME ?= testpypi
PIP ?= pip3

.PHONY: build ci clean install upload

build:
	$(PYTHON) setup.py bdist_wheel sdist

check:
	$(PYTHON) -m twine check dist/*

ci: build
	$(PYTHON) -m unittest discover tests -v
	$(PYTHON) -m tox

clean:
	$(PIP) uninstall gptcli -y
	rm -rf build \
		dist \
		*/*.egg-info

install:
	$(PYTHON) setup.py install

upload: build ci
	$(PYTHON) -m twine upload \
		--config-file $(PYPIRC_CONFIG) \
		--repository $(PYPI_REPO_NAME) dist/*
