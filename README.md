
# Fraud Detection System Using Neural Networks

## Overview
This project is a comprehensive Fraud Detection System that leverages neural networks to identify fraudulent transactions in financial datasets. The system is designed with modularity and scalability in mind, making it easy to extend and maintain. It adheres to object-oriented programming (OOP) principles and utilizes various open-source tools and libraries to streamline the development process.

## Project Structure

The project is organized into several modules, each responsible for a specific part of the workflow. This modular approach allows for better code management and reuse.

```
fraud_detection_system/
│
├── data/
│   ├── data_ingestion.py    # Module for ingesting and streaming data using Kafka
│   ├── preprocess.py        # Module for data preprocessing
│   ├── datasets/            # Directory to store downloaded datasets
│   └── __init__.py          # Init file for the data module
│
├── models/
│   ├── model.py             # Module for defining and training the neural network
│   ├── train.py             # Module to train the model
│   ├── evaluate.py          # Module to evaluate the model
│   └── __init__.py          # Init file for the models module
│
├── database/
│   ├── db_connection.py     # Module to handle database connections
│   ├── db_operations.py     # Module to perform database operations
│   └── __init__.py          # Init file for the database module
│
├── visualization/
│   ├── visualize.py         # Module for visualizing data and results using Redash
│   └── __init__.py          # Init file for the visualization module
│
├── utils/
│   ├── config.py            # Configuration settings for the project
│   └── logger.py            # Logging configuration
│
├── main.py                  # Entry point for the project
├── README.md                # Project documentation
└── requirements.txt         # Required packages
```

## Technologies Used

- **Python**: The core programming language used for this project.
- **PyTorch**: Used for building and training neural networks. It provides a flexible and intuitive framework for deep learning.
- **Apache Kafka**: Employed for streaming transaction data, allowing for real-time data processing.
- **PostgreSQL**: Chosen as the relational database for storing and managing transaction data.
- **Redash**: An open-source tool for querying, visualizing, and sharing data, integrated for data visualization.
- **Kaggle Datasets**: The project utilizes the Credit Card Fraud Detection Dataset and the IEEE-CIS Fraud Detection Dataset, both available on Kaggle.

## Setup Instructions

### 1. Clone the Repository
To get started with the project, clone the repository to your local machine:

```bash
git clone https://github.com/your_username/fraud_detection_system.git
cd fraud_detection_system
```

### 2. Install Required Packages
Ensure all the necessary packages are installed by running:

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Edit the `utils/config.py` file to configure environment variables like database credentials, Kafka topics, and Redash API keys.

### 4. Run the Project
Execute the main script to start the entire workflow, from data ingestion to model evaluation:

```bash
python main.py
```

## Key Features

- **Modular Design**: The project is divided into separate modules for data ingestion, preprocessing, model training, evaluation, and visualization.
- **Scalability**: Designed to handle large-scale datasets and real-time streaming data.
- **OOP Principles**: The codebase follows object-oriented programming practices, making it easy to extend and maintain.
- **Real-time Data Processing**: With Apache Kafka, the system can process streaming data in real-time.
- **Comprehensive Visualization**: Redash is integrated for querying and visualizing the results, making it easier to interpret model performance and data insights.

## Dataset Information

### Credit Card Fraud Detection Dataset
This dataset contains transactions made by credit cards in September 2013 by European cardholders. It presents a binary classification problem with 284,807 transactions, among which 492 are fraudulent.

### IEEE-CIS Fraud Detection Dataset
A more complex dataset provided by Vesta Corporation and hosted on Kaggle. It is intended for advanced fraud detection modeling and features both transactional and identity information.

## Contribution Guidelines

Contributions are welcome! If you would like to contribute, please fork the repository, create a new branch, and submit a pull request with your changes. Ensure that your code adheres to the project's coding standards and passes all tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for more details.

## Contact Information

For any inquiries or issues, please reach out to the project maintainer at lishwanthkumar@gmail.com .

