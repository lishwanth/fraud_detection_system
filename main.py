from data.data_ingestion import DataIngestion
from data.preprocess import Preprocessor
from models.train import ModelTrainer
from models.evaluate import ModelEvaluator
from database.db_connection import DatabaseConnection
from database.db_operations import DatabaseOperations
from visualization.visualize import DataVisualizer
from utils.config import Config
from utils.logger import Logger

def main():
    logger = Logger.get_logger('fraud_detection')

    # Data Ingestion
    logger.info('Starting data ingestion...')
    ingestion = DataIngestion(Config.KAFKA_TOPIC, Config.KAFKA_SERVERS)
    ingestion.send_data('data/datasets/credit_card_fraud.csv')
    logger.info('Data ingestion completed.')

    # Data Preprocessing
    logger.info('Starting data preprocessing...')
    data = pd.read_csv('data/datasets/credit_card_fraud.csv')
    preprocessor = Preprocessor()
    processed_data = preprocessor.preprocess(data)
    pd.DataFrame(processed_data).to_csv('data/datasets/processed_data.csv', index=False)
    logger.info('Data preprocessing completed.')

    # Model Training
    logger.info('Starting model training...')
    model = FraudDetectionModel(input_size=processed_data.shape[1])
    trainer = ModelTrainer(model)
    trainer.train(train_loader, epochs=10)
    logger.info('Model training completed.')

    # Model Evaluation
    logger.info('Starting model evaluation...')
    evaluator = ModelEvaluator(model)
    accuracy, cm = evaluator.evaluate(test_loader)
    logger.info(f'Accuracy: {accuracy}')
    logger.info(f'Confusion Matrix:\n{cm}')

    # Visualization
    logger.info('Starting visualization...')
    visualizer = DataVisualizer(Config.REDASH_API_KEY, Config.REDASH_URL)
    visualizer.visualize(query_id=1)
    logger.info('Visualization completed.')

if __name__ == "__main__":
    main()
