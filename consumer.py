import json
from kafka import KafkaConsumer

if __name__ == '__main__':
    # Kafka Consumer
    consumerOfTopicOne = KafkaConsumer(
        'tesla',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest'
    )

    consumerOfTopicTwo = KafkaConsumer(
        'apple',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest'
    )

    for message in consumerOfTopicOne:
        print(json.loads(message.value))

    for message in consumerOfTopicTwo:
        print(json.loads(message.value))