//go:build tools

package tools

var (
	_ = "github.com/bufbuild/buf/cmd/buf@v1.50.1"
	_ = "github.com/fullstorydev/grpcurl/cmd/grpcurl@v1.9.3"
	_ = "github.com/grpc-ecosystem/grpc-gateway/v2/protoc-gen-grpc-gateway@v2.26.3"
	_ = "github.com/grpc-ecosystem/grpc-gateway/v2/protoc-gen-openapiv2@v2.26.3"
	_ = "google.golang.org/grpc/cmd/protoc-gen-go-grpc@v1.5.1"
	_ = "google.golang.org/protobuf/cmd/protoc-gen-go@v1.36.5"
)
