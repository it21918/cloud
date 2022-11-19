import json
from kafka import KafkaConsumer

if __name__ == '__main__':
    topics = ['tesla', 'apple', 'microsoft', 'nasa', 'amazon', 'BBC', 'cloud', 'fiat'] 

    # Kafka Consumer
    consumerOfTopicOne = KafkaConsumer(
        *topics,
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest'
    )

    consumerOfTopicTwo = KafkaConsumer(
        'sourcesDomainName',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest'
    )

    for message in consumerOfTopicTwo:
        print(json.loads(message.value))

