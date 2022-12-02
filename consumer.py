import json
from kafka import KafkaConsumer
from kafka.structs import TopicPartition
from pymongo_get_database import get_database


if __name__ == '__main__':
    dbname = get_database()
    collection_name = dbname["domain_name_description"]
    

    topics = ['tesla', 'apple', 'microsoft', 'nasa', 'amazon', 'BBC', 'cloud', 'fiat'] 

    # Kafka Consumer
    consumerOfTopics = KafkaConsumer(
        *topics,
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest'
    )

    consumerOfDomainNames = KafkaConsumer(
        'sourcesDomainName',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest'
    )


    for message in consumerOfDomainNames:
        print(json.loads(message.value))
        #item_1 = {"source_domain_name" : 1}
        collection_name.insert_one(json.loads(message.value))
        #collection_name.insert_many([item_1])

    # for message in consumerOfTopics:
    #     record = json.loads(message.value)

    #     if message.topic == 'apple' :
    #         print(json.loads(message.value))

    #         for msg in consumer:
    #             record = json.loads(msg.value)
    #             name = record['name']
    #             shop = record['shop']
    #             phoneNumber = record['phoneNumber']
    #             address = record['phoneNumber']
    #             pizzas = record['pizzas']
                
    #             # Create dictionary and ingest data into MongoDB
    #             try:
    #             pizza_rec = {'name':name,'shop':shop,'phoneNumber':phoneNumber,'address':address,'pizzas' :pizzas}
    #             rec_id1 = db.coba_info.insert_one(pizza_rec)
    #             print("Data inserted with record ids", rec_id1)
    #             except:
    #             print("Could not insert into MongoDB")





