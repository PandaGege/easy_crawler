# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import crawler_pb2 as crawler__pb2


class CrawlerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.request = channel.unary_unary(
        '/Crawler/request',
        request_serializer=crawler__pb2.CrawlerRequest.SerializeToString,
        response_deserializer=crawler__pb2.CrawlerResponse.FromString,
        )


class CrawlerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def request(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CrawlerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'request': grpc.unary_unary_rpc_method_handler(
          servicer.request,
          request_deserializer=crawler__pb2.CrawlerRequest.FromString,
          response_serializer=crawler__pb2.CrawlerResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Crawler', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
