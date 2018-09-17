# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from proto import hello_pb2 as proto_dot_hello__pb2


class gRPCStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SayHello = channel.unary_unary(
        '/example.gRPC/SayHello',
        request_serializer=proto_dot_hello__pb2.HelloRequest.SerializeToString,
        response_deserializer=proto_dot_hello__pb2.HelloReply.FromString,
        )


class gRPCServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SayHello(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_gRPCServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SayHello': grpc.unary_unary_rpc_method_handler(
          servicer.SayHello,
          request_deserializer=proto_dot_hello__pb2.HelloRequest.FromString,
          response_serializer=proto_dot_hello__pb2.HelloReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'example.gRPC', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))