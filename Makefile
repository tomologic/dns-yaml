build:
	docker build -t tomologic/dns-yaml .

run:
	docker run -v "$(PWD):/input" --rm tomologic/dns-yaml /input/example.yaml

.PHONY: build run
