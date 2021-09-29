import grpc
from concurrent import futures
import collector_pb2_grpc
import collector_pb2

class Collector(collector_pb2_grpc.CollectorServicer):
    
    def SendReading(self, request, context):
        print(request.temperature)
        print(request.humidity)
        return collector_pb2.CollectorResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    collector_pb2_grpc.add_CollectorServicer_to_server(Collector(), server)
    server.add_insecure_port('[::]:8080')
    server.start()
    print("Started listening..")
    server.wait_for_termination()

serve()