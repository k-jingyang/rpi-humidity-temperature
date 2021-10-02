FROM python:3.9-slim

WORKDIR /collector

COPY collector.py .
COPY collector_pb2_grpc.py .
COPY collector_pb2.py .
COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT [ "python3", "collector.py" ]