SHELL = /usr/bin/env bash -euo pipefail

outdir := ../pb

# These are the input proto files, i.e. what is going to be compiled
proto_files := $(shell find . -name '*.proto')

# Helper vars for proto dependencies (i.e. what are used in any referenced imports)
proto_deps_rootdir := /tmp/proto-deps
proto_deps_sources :=	\
	github.com/googleapis/googleapis \
	github.com/protocolbuffers/protobuf
proto_deps_import_flags := \
	-I=. \
	-I=$(proto_deps_rootdir)/github.com/googleapis/googleapis \
	-I=$(proto_deps_rootdir)/github.com/protocolbuffers/protobuf/src \

# So that the Python generation works off of the virtual environment's dependencies
pyvenv = source ../venv/bin/activate

get-proto-deps:
	@mkdir -p /tmp/proto-deps
	@for dep in $(proto_deps_sources) ; do \
		if [[ ! -d $(proto_deps_rootdir)/"$${dep}" ]] ; then \
			git clone --depth=1 https://"$${dep}" $(proto_deps_rootdir)/"$${dep}" || true ; \
		fi ; \
	done

ensure-outdir:
	@mkdir -p $(outdir)

# This is a WAY heavier protoc call than you'd probably see in real life, but
# this demonstrates how many outputs & options you can provide.
#
# Most lang/output code can be generated directly by a single call to protoc
# with available plugins ...
gen: get-proto-deps ensure-outdir
	@printf 'Generating protobuf code...\n'
	@$(pyvenv) && \
	protoc \
		$(proto_deps_import_flags) \
		--go_out=$(outdir) \
		--go_opt=paths=source_relative \
		\
		--go-grpc_out=$(outdir) \
		--go-grpc_opt=paths=source_relative \
		--go-grpc_opt=require_unimplemented_servers=false \
		\
		--grpc-gateway_out=$(outdir) \
		--grpc-gateway_opt=logtostderr=true \
    --grpc-gateway_opt=paths=source_relative \
    --grpc-gateway_opt=generate_unbound_methods=true \
		\
		--openapi_out=$(outdir) \
		--openapi_opt=output_mode=source_relative \
		\
		--python_out=$(outdir) \
		--pyi_out=$(outdir) \
		\
		--descriptor_set_out=./protoset \
		--include_imports \
		\
		$(proto_files)
# ... but Python gRPC seems to be an angry elf, so we have to use a protoc
# distro that's in the grpcio_tools Python module
	@printf 'Generating Python gRPC code, specifically...\n'
	@$(pyvenv) && \
	python3 -m grpc_tools.protoc \
		$(proto_deps_import_flags) \
		--grpc_python_out=$(outdir) \
		$(proto_files)
# AND ALSO we need to modify an import line in the generated code, or else that
# code's module pathing won't work as-generated. It would work if the proto
# file(s) AND the generated output were in the same directory, but we don't have
# our tree set up that way
	@printf 'Fixing Python import statements...\n'
	@find $(outdir) -type f -name '*.py' | xargs -I{} sed -E -i 's/^from .*\.v[0-9]+ import (.*)/from . import \1/g' {}

# These targets show that you can use a custom-built protoc plugin to generate
# code from proto defs however you want!
build-custom-plugin:
	@make -s -C ../protoc-gen-bash build

gen-custom: get-proto-deps ensure-outdir build-custom-plugin
	@printf 'Generating code using custom protoc plugin...\n'
	@protoc \
		--plugin=../protoc-gen-bash/build/protoc-gen-bash \
		$(proto_deps_import_flags) \
		--bash_out=$(outdir) \
		--bash_opt=paths=source_relative \
		$(proto_files)

lint:
	@go run github.com/bufbuild/buf/cmd/buf@latest lint
