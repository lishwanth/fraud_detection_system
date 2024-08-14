import pandas as pd
from sklearn.preprocessing import StandardScaler

class Preprocessor:
    def __init__(self):
        self.scaler = StandardScaler()

    def preprocess(self, data):
        data = data.dropna()
        data = pd.get_dummies(data, drop_first=True)
        scaled_data = self.scaler.fit_transform(data)
        return scaled_data

if __name__ == "__main__":
    file_path = 'data/datasets/credit_card_fraud.csv'
    data = pd.read_csv(file_path)
    
    preprocessor = Preprocessor()
    processed_data = preprocessor.preprocess(data)
    pd.DataFrame(processed_data).to_csv('data/datasets/processed_data.csv', index=False)
