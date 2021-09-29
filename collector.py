import grpc
from concurrent import futures
import collector_pb2_grpc
import collector_pb2
import pandas as pd
from fastparquet import write

# Should the Parquet file contain time too? Are timestamps treated specially as compared to normal data?

_PERSIST_INTERVAL = 10


class Collector(collector_pb2_grpc.CollectorServicer):

    def __init__(self):
        self.tick = 0
        self.data = []

    def SendReading(self, request, context):
        temperature = request.temperature
        humidity = request.humidity
        self.tick+=1

        if self.tick % _PERSIST_INTERVAL == 0:
            df = pd.DataFrame(self.data,  columns=["humidity", "temperature"])

            # How to append to Parquet file? You can't
            write('outfile.parquet', df)
            self.data = []
            self.tick = 0 

        return collector_pb2.CollectorResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    collector_pb2_grpc.add_CollectorServicer_to_server(Collector(), server)
    server.add_insecure_port('[::]:8080')
    server.start()
    print("Started listening..")
    server.wait_for_termination()


serve()
