import threading
import json
from datetime import datetime

from kafka import KafkaConsumer
from transaction import Transaction
from database import Session


class Consumer(threading.Thread):
    def __init__(self, topics):
        threading.Thread.__init__(self)
        self.topics = topics
        self.stop_event = threading.Event()

    def stop(self):
        self.stop_event.set()

    def run(self):
        consumer = KafkaConsumer(
            bootstrap_servers=['localhost:29092'],
            auto_offset_reset='earliest',
            consumer_timeout_ms=1000,
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )
        print(f'subscribing to {self.topics}')
        consumer.subscribe(self.topics)

        while not self.stop_event.is_set():
            for message in consumer:
                id, user_id, amount, created_at = message.value.values()
                print(
                    f'message received: {id}, {user_id}, {amount}, {created_at}')
                transaction = Transaction(
                    id, user_id, amount, datetime.fromtimestamp(float(created_at)))
                session = Session()
                session.add(transaction)
                try:
                    session.commit()
                except Exception as e:
                    print("failed to save transaction", e)
        consumer.close()
