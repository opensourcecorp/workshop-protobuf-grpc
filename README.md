# Protocol Buffers & gRPC

## TODO: THIS WORKSHOP IS NOT READY YET

This repository contains samples that generate code using [protocol
buffers](https://developers.google.com/protocol-buffers) in several different
languages, and defines a server & client in each to demonstrate
[gRPC](https://grpc.io) calls against the server regardless of which language
it's running in. For the Go server, it also demonstrates that you are able to
serve gRPC as well as HTTP requests from the same server program.

## How to Use

First, set up your workstation with some required tools via:

    make setup

The proto definitions are found under the `proto/` directory, organized
according to what is deemed best-practice -- the proto package name, and version
number. Protocol buffers themselves are generated via:

    make generate

run from either this root directory or the `proto/` directory. You can inspect
the `proto/Makefile` to see the commands needed to generate the code.

To generate code using the custom plugin defined in `protoc-gen-bash`, you can
run:

    make gen-custom

All generated protobuf code itself is stored in the `generated/` directory tree.

One of the plugins used (`protoc-gen-openapi`) generates OpenAPI/Swagger specs.
You can view those in a more human-readable way by pasting them
[here](https://editor.swagger.io/), for example.
