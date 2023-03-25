PYTHON ?= python3
PYPIRC_CONFIG ?= $(HOME)/.pypirc
PYPI_REPO_NAME ?= testpypi
PIP ?= pip3
TWINE='twine>=4.0.2'
BUILD='build>=0.10.0'

.PHONY: build ci clean install upload

build:
	$(PIP) install --upgrade $(BUILD)
	$(PYTHON) -m build

check: build
	$(PIP) install --upgrade $(TWINE)
	$(PYTHON) -m twine check dist/*

ci: build
	$(PIP) install --upgrade $(TWINE)
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
	$(PIP) install --upgrade $(TWINE)
	$(PYTHON) -m twine upload \
		--config-file $(PYPIRC_CONFIG) \
		--repository $(PYPI_REPO_NAME) dist/*
