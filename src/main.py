import logging

from kafka import KafkaAdminClient
from kafka.admin import NewTopic
from producer import Producer
from subscriber import Consumer
from database import Base, engine
import logging

logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
logging.basicConfig(level=logging.INFO)

TOPIC = 'some-topics'

def pubsub():
    try:
        admin = KafkaAdminClient(bootstrap_servers=['localhost:29092'])
        topic = NewTopic(name=TOPIC,
                         num_partitions=1,
                         replication_factor=1)
        admin.create_topics([topic])
    except Exception:
        pass

    tasks = [
        Producer(TOPIC),
        Consumer([TOPIC])
    ]

    # Start threads of a publisher/producer and a subscriber/consumer to 'my-topic' Kafka topic
    for t in tasks:
        t.start()

def create_tables():
    print('preparing tables')
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()
    pubsub()
