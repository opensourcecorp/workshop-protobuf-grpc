package main

import (
	"context"
	"strings"

	"github.com/bufbuild/protoplugin"
	"google.golang.org/protobuf/types/descriptorpb"
)

const version = "0.0.1"

func main() {
	protoplugin.Main(protoplugin.HandlerFunc(handle), protoplugin.WithVersion(version))
}

func handle(
	_ context.Context,
	_ protoplugin.PluginEnv,
	responseWriter protoplugin.ResponseWriter,
	request protoplugin.Request,
) error {
	// Set the flag indicating that we support proto3 optionals. We don't even use them in this
	// plugin, but protoc will error if it encounters a proto3 file with an optional but the
	// plugin has not indicated it will support it.
	responseWriter.SetFeatureProto3Optional()
	responseWriter.SetFeatureSupportsEditions(descriptorpb.Edition_EDITION_2023, descriptorpb.Edition_EDITION_2023)

	for _, fileDescriptorProto := range request.FileDescriptorProtosToGenerate() {
		topLevelMessageNames := make([]string, len(fileDescriptorProto.GetMessageType()))
		for i, descriptorProto := range fileDescriptorProto.GetMessageType() {
			topLevelMessageNames[i] = descriptorProto.GetName()
		}
		// Add the response file to the response.
		responseWriter.AddFile(
			fileDescriptorProto.GetName()+".txt",
			strings.Join(topLevelMessageNames, "\n")+"\n",
		)
	}

	return nil
}
