import time
import json
from datetime import datetime
from data_generator import  get_articles, mediaWiki
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

        topics = ['tesla', 'apple', 'microsoft', 'nasa', 'amazon', 'BBC', 'cloud', 'fiat'] 

        # Send article to our consumer
        for topic in topics:
            ##print(f'Producing message @ {datetime.now()} | Message = {str(get_articles(topic))}')
            articles, description = get_articles(topic)
            producer.send(topic,  articles)
            producer.send('sourcesDomainName', description)

        # Sleep for two hours
        time_to_sleep = 3600 * 1000
        time.sleep(time_to_sleep)