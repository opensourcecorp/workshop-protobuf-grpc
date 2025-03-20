SHELL = /usr/bin/env bash -euo pipefail

# Needed so that the Python generation works off of the virtual environment's
# dependencies
pyvenv = source ../venv/bin/activate

generate: build-custom-plugin
	$(pyvenv) && buf generate
# AND ALSO we need to modify an import line in the generated code, or else that
# code's module pathing won't work as-generated. It would work if the proto
# file(s) AND the generated output were in the same directory, but we don't have
# our tree set up that way
#	@printf 'Fixing Python import statements...\n'
#	@find ../generated/python -type f -name '*.py' | xargs -I{} sed -E -i 's/^from .*\.v[0-9]+ import (.*)/from . import \1/g' {}

# These targets show that you can use a custom-built protoc plugin to generate
# code from proto defs however you want!
build-custom-plugin:
	@make -s -C ../protoc-gen-bash/ build
	@make -s -C ../protoc-gen-bash/v2/ build

lint:
	@buf lint
