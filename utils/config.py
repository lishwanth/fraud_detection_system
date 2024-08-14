import os

class Config:
    KAFKA_TOPIC = os.getenv('KAFKA_TOPIC', 'fraud_detection')
    KAFKA_SERVERS = os.getenv('KAFKA_SERVERS', 'localhost:9092')
    DATABASE = {
        'dbname': os.getenv('DB_NAME', 'fraud_db'),
        'user': os.getenv('DB_USER', 'user'),
        'password': os.getenv('DB_PASSWORD', 'password'),
        'host': os.getenv('DB_HOST', 'localhost'),
        'port': os.getenv('DB_PORT', '5432'),
    }
    REDASH_API_KEY = os.getenv('REDASH_API_KEY', 'your_redash_api_key')
    REDASH_URL = os.getenv('REDASH_URL', 'http://localhost:5000')
