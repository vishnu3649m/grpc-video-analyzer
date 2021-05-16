# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import image_detection_pb2 as image__detection__pb2


class ImageDetectionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetDetectableObjects = channel.unary_unary(
                '/ObjDet.Grpc.ImageDetection/GetDetectableObjects',
                request_serializer=image__detection__pb2.DetectableObjectsRequest.SerializeToString,
                response_deserializer=image__detection__pb2.DetectableObjectsResponse.FromString,
                )
        self.DetectImage = channel.unary_unary(
                '/ObjDet.Grpc.ImageDetection/DetectImage',
                request_serializer=image__detection__pb2.ImageDetectionRequest.SerializeToString,
                response_deserializer=image__detection__pb2.ImageDetectionResponse.FromString,
                )


class ImageDetectionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetDetectableObjects(self, request, context):
        """*
        Returns the list of objects detectable by object detection model(s) in the server.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DetectImage(self, request, context):
        """*
        Runs object detector(s) on the provided image and returns detections.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ImageDetectionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetDetectableObjects': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDetectableObjects,
                    request_deserializer=image__detection__pb2.DetectableObjectsRequest.FromString,
                    response_serializer=image__detection__pb2.DetectableObjectsResponse.SerializeToString,
            ),
            'DetectImage': grpc.unary_unary_rpc_method_handler(
                    servicer.DetectImage,
                    request_deserializer=image__detection__pb2.ImageDetectionRequest.FromString,
                    response_serializer=image__detection__pb2.ImageDetectionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ObjDet.Grpc.ImageDetection', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ImageDetection(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetDetectableObjects(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ObjDet.Grpc.ImageDetection/GetDetectableObjects',
            image__detection__pb2.DetectableObjectsRequest.SerializeToString,
            image__detection__pb2.DetectableObjectsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DetectImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ObjDet.Grpc.ImageDetection/DetectImage',
            image__detection__pb2.ImageDetectionRequest.SerializeToString,
            image__detection__pb2.ImageDetectionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
