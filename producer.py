import time
import json
from datetime import datetime
from data_generator import generate_message, get_articles
from kafka import KafkaProducer


# Messages will be serialized as JSON
def serializer(message):
    return json.dumps(message).encode('utf-8')


# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=serializer
)

if __name__ == '__main__':
    # Infinite loop - runs until you kill the program
    while True:

        topics = ['tesla', 'apple']

        # Send article to our consumer
        for topic in topics:
            print(f'Producing message @ {datetime.now()} | Message = {str(get_articles(topic))}')
            producer.send(topic, get_articles(topic))

        # Sleep for a random number of seconds
        time_to_sleep = 3600 * 1000
        time.sleep(time_to_sleep)