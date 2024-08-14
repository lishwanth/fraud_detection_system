import kafka
from kafka import KafkaProducer, KafkaConsumer
import pandas as pd

class DataIngestion:
    def __init__(self, kafka_topic, kafka_servers):
        self.producer = KafkaProducer(bootstrap_servers=kafka_servers)
        self.topic = kafka_topic

    def send_data(self, file_path):
        data = pd.read_csv(file_path)
        for _, row in data.iterrows():
            message = row.to_json().encode('utf-8')
            self.producer.send(self.topic, message)
        self.producer.flush()

if __name__ == "__main__":
    kafka_topic = 'fraud_detection'
    kafka_servers = ['localhost:9092']
    file_path = 'data/datasets/credit_card_fraud.csv'

    ingestion = DataIngestion(kafka_topic, kafka_servers)
    ingestion.send_data(file_path)
