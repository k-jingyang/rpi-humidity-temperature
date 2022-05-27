build:
	docker build -t collector:local .

clean:
	docker rmi collector:local