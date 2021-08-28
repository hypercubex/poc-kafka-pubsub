# README

Kafka setup referenced from this tutorial<https://www.baeldung.com/ops/kafka-docker-setup>

## How to start

1. Please rename .env.example to .env
1. `docker compose up --build -d` (topic 'some-topics', database 'test' with table 'some-topics' will be created automatically)
1. cd pubsub
1. `pipenv install`
1. `pipenv run python3 src/main.py` # may need to wait for kafka fully started

## Components included

- docker images with Kafka for streaming
- Postgres db
- a producer that publishes messages to Kafka via streaming randomly within 2 seconds
- a subscriber to consume the messages from the stream and writes to the postgres db
