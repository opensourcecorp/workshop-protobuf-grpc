SHELL = /usr/bin/env bash -euo pipefail

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
	-I=$(proto_deps_rootdir)/github.com/protocolbuffers/protobuf/src

# Needed so that the Python generation works off of the virtual environment's
# dependencies
pyvenv-activate = source ../venv/bin/activate

get-proto-deps:
	@mkdir -p /tmp/proto-deps
	@for dep in $(proto_deps_sources) ; do \
		if [[ ! -d $(proto_deps_rootdir)/"$${dep}" ]] ; then \
			git clone --depth=1 https://"$${dep}" $(proto_deps_rootdir)/"$${dep}" || true ; \
		fi ; \
	done

outdir := ../generated
outdir_go := $(outdir)/go
outdir_py := $(outdir)/python
outdir_openapi := $(outdir)/openapi
outdir_bash := $(outdir)/bash

ensure-outdirs:
	@mkdir -p \
		$(outdir) \
		$(outdir_go) \
		$(outdir_py) \
		$(outdir_openapi) \
		$(outdir_bash)

# This is a WAY heavier protoc call than you'd probably see in real life, but
# this demonstrates how many outputs & options you can provide.
#
# Notes for each codegen flag block are as follows, since you can't
# inline-comment a multiline shell command:
#
# --go*: Options for pure Go
#
# --go-grpc*: Options for Go gRPC
#
# --grpc-gateway*: Options for Go gRPC-HTTP transcoding gateway
#
# --openapi*: Options for OpenAPI specification
#
# --python*/pyi*: Options for Python
#
# --descriptor_set_out/include_imports: Generates a `protoset` file that can be
# used by some tools to make determining the contents of a Protobuf
# specification easier when encountering a binary representation
generate: get-proto-deps ensure-outdirs
	@printf 'Generating protobuf code...\n'
	@$(pyvenv-activate) && \
	protoc \
		$(proto_deps_import_flags) \
		--go_out=$(outdir_go) \
		--go_opt=paths=source_relative \
		\
		--go-grpc_out=$(outdir_go) \
		--go-grpc_opt=paths=source_relative \
		--go-grpc_opt=require_unimplemented_servers=false \
		\
		--grpc-gateway_out=$(outdir_go) \
		--grpc-gateway_opt=logtostderr=true \
    --grpc-gateway_opt=paths=source_relative \
    --grpc-gateway_opt=generate_unbound_methods=true \
		\
		--openapi_out=$(outdir_openapi) \
		--openapi_opt=output_mode=source_relative \
		\
		--python_out=$(outdir_py) \
		--pyi_out=$(outdir_py) \
		\
		--descriptor_set_out=./protoset \
		--include_imports \
		\
		$(proto_files)
# ... but Python gRPC seems to be an angry elf, so we have to use a protoc
# distro that's in the grpcio_tools Python module
	@printf 'Generating Python gRPC code, specifically...\n'
	@$(pyvenv-activate) && \
	python3 -m grpc_tools.protoc \
		$(proto_deps_import_flags) \
		--grpc_python_out=$(outdir_py) \
		$(proto_files)
# AND ALSO we need to modify an import line in the generated code, or else that
# code's module pathing won't work as-generated. It would work if the proto
# file(s) AND the generated output were in the same directory, but we don't have
# our tree set up that way
	@printf 'Fixing Python import statements...\n'
	@find $(outdir_py) -type f -name '*.py' | xargs -I{} sed -E -i 's/^from .*\.v[0-9]+ import (.*)/from . import \1/g' {}

# These targets show that you can use a custom-built protoc plugin to generate
# code from proto defs however you want!
build-custom-plugin:
	@make -s -C ../protoc-gen-bash build

generate-custom: get-proto-deps ensure-outdirs build-custom-plugin
	@printf 'Generating code using custom protoc plugin...\n'
	@protoc \
		--plugin=../protoc-gen-bash/build/protoc-gen-bash \
		$(proto_deps_import_flags) \
		--bash_out=$(outdir_bash) \
		--bash_opt=paths=source_relative \
		$(proto_files)

lint:
	@go run github.com/bufbuild/buf/cmd/buf@latest lint
