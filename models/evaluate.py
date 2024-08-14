import torch
from sklearn.metrics import accuracy_score, confusion_matrix
import pandas as pd
from .model import FraudDetectionModel

class ModelEvaluator:
    def __init__(self, model):
        self.model = model

    def evaluate(self, test_loader):
        all_preds = []
        all_labels = []

        with torch.no_grad():
            for batch in test_loader:
                inputs, labels = batch
                outputs = self.model(inputs)
                preds = outputs.round()
                all_preds.extend(preds.numpy())
                all_labels.extend(labels.numpy())

        accuracy = accuracy_score(all_labels, all_preds)
        cm = confusion_matrix(all_labels, all_preds)
        return accuracy, cm

if __name__ == "__main__":
    data = pd.read_csv('data/datasets/processed_data.csv')
    inputs = torch.tensor(data.iloc[:, :-1].values, dtype=torch.float32)
    labels = torch.tensor(data.iloc[:, -1].values, dtype=torch.float32).unsqueeze(1)

    dataset = TensorDataset(inputs, labels)
    test_loader = DataLoader(dataset, batch_size=64, shuffle=False)

    model = FraudDetectionModel(input_size=inputs.shape[1])
    model.load_state_dict(torch.load('models/fraud_detection_model.pth'))

    evaluator = ModelEvaluator(model)
    accuracy, cm = evaluator.evaluate(test_loader)
    print(f"Accuracy: {accuracy}")
    print(f"Confusion Matrix:\n{cm}")
