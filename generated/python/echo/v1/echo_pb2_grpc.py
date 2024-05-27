# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import echo_pb2 as echo_dot_v1_dot_echo__pb2


class EchoServiceStub(object):
    """TODO: once I figure out how Java works lol
    // You also need to specify any other appropriate static options for other
    // languages; here's where you specify the Java package name, for example
    option java_package = "org.opensourcecorp.workshops.protobuf_grpc.echo.v1";

    Service that shows a few ways to work with protobufs and gRPC
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Echo = channel.unary_unary(
                '/echo.v1.EchoService/Echo',
                request_serializer=echo_dot_v1_dot_echo__pb2.EchoRequest.SerializeToString,
                response_deserializer=echo_dot_v1_dot_echo__pb2.EchoResponse.FromString,
                )


class EchoServiceServicer(object):
    """TODO: once I figure out how Java works lol
    // You also need to specify any other appropriate static options for other
    // languages; here's where you specify the Java package name, for example
    option java_package = "org.opensourcecorp.workshops.protobuf_grpc.echo.v1";

    Service that shows a few ways to work with protobufs and gRPC
    """

    def Echo(self, request, context):
        """Echo responds to the caller with the same message they sent
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EchoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Echo': grpc.unary_unary_rpc_method_handler(
                    servicer.Echo,
                    request_deserializer=echo_dot_v1_dot_echo__pb2.EchoRequest.FromString,
                    response_serializer=echo_dot_v1_dot_echo__pb2.EchoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'echo.v1.EchoService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EchoService(object):
    """TODO: once I figure out how Java works lol
    // You also need to specify any other appropriate static options for other
    // languages; here's where you specify the Java package name, for example
    option java_package = "org.opensourcecorp.workshops.protobuf_grpc.echo.v1";

    Service that shows a few ways to work with protobufs and gRPC
    """

    @staticmethod
    def Echo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/echo.v1.EchoService/Echo',
            echo_dot_v1_dot_echo__pb2.EchoRequest.SerializeToString,
            echo_dot_v1_dot_echo__pb2.EchoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)