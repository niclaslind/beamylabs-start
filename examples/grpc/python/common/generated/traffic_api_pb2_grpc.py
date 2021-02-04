# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import traffic_api_pb2 as traffic__api__pb2


class TrafficServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.StartPlayback = channel.stream_stream(
        '/base.TrafficService/StartPlayback',
        request_serializer=traffic__api__pb2.PlaybackInfos.SerializeToString,
        response_deserializer=traffic__api__pb2.PlayBackStatuses.FromString,
        )


class TrafficServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def StartPlayback(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TrafficServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'StartPlayback': grpc.stream_stream_rpc_method_handler(
          servicer.StartPlayback,
          request_deserializer=traffic__api__pb2.PlaybackInfos.FromString,
          response_serializer=traffic__api__pb2.PlayBackStatuses.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'base.TrafficService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))