PACKAGE_NAME=nethsm
VENV=venv
PYTHON3=python3
PYTHON3_VENV=venv/bin/python3
FLAKE8_DIRS=$(PACKAGE_NAME)/

all: init

init: update-venv

# code checks
check-format:
	$(PYTHON3_VENV) -m black --check $(PACKAGE_NAME)/

check-import-sorting:
	$(PYTHON3_VENV) -m isort --check-only $(PACKAGE_NAME)/

check-style:
	$(PYTHON3_VENV) -m flake8 $(FLAKE8_DIRS)

check-typing:
	@echo "Note: run semi-clean target in case this fails without any proper reason"
	$(PYTHON3_VENV) -m mypy $(PACKAGE_NAME)/

check: check-format check-import-sorting check-style check-typing test 

semi-clean:
	rm -rf ./**/__pycache__
	rm -rf ./.mypy_cache

clean: semi-clean
	rm -rf ./$(VENV)
	rm -rf ./dist

# automatic code fixes
fix:
	$(PYTHON3_VENV) -m black $(BLACK_FLAGS) $(PACKAGE_NAME)/ tests/
	$(PYTHON3_VENV) -m isort $(ISORT_FLAGS) $(PACKAGE_NAME)/ tests/

$(VENV):
	$(PYTHON3) -m venv $(VENV)
	$(PYTHON3_VENV) -m pip install -U pip

update-venv: $(VENV)
	$(PYTHON3_VENV) -m pip install -U pip
	$(PYTHON3_VENV) -m pip install flit
	$(PYTHON3_VENV) -m flit install --symlink


OPENAPI_OUTPUT_DIR=${PWD}/tmp/openapi-client

nethsm-api.yaml:
	curl "https://nethsmdemo.nitrokey.com/api_docs/nethsm-api.yaml" --output nethsm-api.yaml

# Generates the OpenAPI client for the NetHSM REST API
# Currently using tag latest because the 3.0.0 tag has problem.
# Hash of the current latest tag (19/09/2023): 880ff39e9610bc379e68da03de91f20af51d5242f19bc9c29ac04f763c480f82
.PHONY: nethsm-client
nethsm-client: nethsm-api.yaml
	mkdir -p "${OPENAPI_OUTPUT_DIR}"
	python tools/transform_nethsm_api_spec.py nethsm-api.yaml "${OPENAPI_OUTPUT_DIR}/nethsm-api.json"
	docker run --rm -ti -v "${OPENAPI_OUTPUT_DIR}:/out" \
		openapijsonschematools/openapi-json-schema-generator-cli:latest generate \
		-i=/out/nethsm-api.json \
		-g=python -o=/out/python --package-name=nethsm.client
	cp -r "${OPENAPI_OUTPUT_DIR}/python/src/nethsm/client" nethsm

.PHONY: test
test:
	$(PYTHON3_VENV) -m pytest --cov nethsm --cov-report=xml