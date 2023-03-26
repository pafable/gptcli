PYTHON ?= python3
PYPI_REPO_URL ?= 'https://test.pypi.org/legacy/'
PIP ?= pip3
TWINE ?= 'twine>=4.0.2'
BUILD ?= 'build>=0.10.0'
TOX ?= 'tox>=4.4.7'

.PHONY: build ci clean install upload

build: upgrade
	$(PIP) install --upgrade $(BUILD)
	$(PYTHON) -m build

check: build ci
	$(PIP) install --upgrade $(TWINE)
	$(PYTHON) -m twine check dist/*

ci:
	$(PIP) install --upgrade $(TOX)
	$(PYTHON) -m tox

clean:
	$(PIP) uninstall gptcli -y
	rm -rf build \
		dist \
		*/*.egg-info

install: upgrade
	$(PIP) install .

upgrade:
	$(PYTHON) -m pip install --upgrade pip

upload: check
	$(PYTHON) -m twine upload --verbose \
		--repository-url $(PYPI_REPO_URL) dist/*
