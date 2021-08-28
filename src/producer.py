import threading
import time
import random
import json
import uuid
import datetime

from kafka import KafkaProducer


class Producer(threading.Thread):
    def __init__(self, topic):
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()
        self.topic = topic

    def stop(self):
        self.stop_event.set()

    def run(self):
        producer = KafkaProducer(bootstrap_servers=['localhost:29092'],
                                 value_serializer=lambda m: json.dumps(m).encode('utf-8'))

        while not self.stop_event.is_set():
            delayTime = random.uniform(0, 1)
            print(f'next message delayTime = {delayTime}')
            time.sleep(delayTime)
            transaction = {
                'id': str(uuid.uuid4()),
                'user_id': random.randint(100000, 100100),
                # $10 - 100 (in terms of cents)
                'amount': random.randint(1000, 10000),
                'created_at': datetime.datetime.now().timestamp()
            }
            print(f'sending transaction {transaction}')
            producer.send(self.topic, transaction)

        producer.close()
