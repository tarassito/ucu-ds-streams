import logging
import os
import pandas as pd
from kafka import KafkaProducer

logging.basicConfig(level=logging.INFO)

HOST = os.getenv("HOST", 'localhost')
PORT = os.getenv("PORT", '8097')
TOPIC = os.getenv("TOPIC", 'browser-history')


def on_send_success(record_metadata):
    logging.info('Producer sent message to topic:partition:offset - %s:%d:%d',
                 record_metadata.topic, record_metadata.partition, record_metadata.offset)


def produce_data():
    producer = KafkaProducer(bootstrap_servers=[f'{HOST}:{PORT}'])
    data = pd.read_csv('history.csv', encoding='utf-8',
                       usecols=['url'])

    print(data.head())

    for index, row in data.iterrows():
        message = ','.join([str(elem) for elem in list(row)])
        producer.send(TOPIC, str(message).encode('utf-8')).add_callback(on_send_success)

    producer.flush()


if __name__ == '__main__':
    produce_data()
