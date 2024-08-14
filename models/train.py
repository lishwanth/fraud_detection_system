import torch
import torch.optim as optim
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from .model import FraudDetectionModel
import pandas as pd

class ModelTrainer:
    def __init__(self, model, learning_rate=0.001):
        self.model = model
        self.criterion = nn.BCELoss()
        self.optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    def train(self, train_loader, epochs):
        for epoch in range(epochs):
            for batch in train_loader:
                inputs, labels = batch
                self.optimizer.zero_grad()
                outputs = self.model(inputs)
                loss = self.criterion(outputs, labels)
                loss.backward()
                self.optimizer.step()
            print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item()}")

if __name__ == "__main__":
    data = pd.read_csv('data/datasets/processed_data.csv')
    inputs = torch.tensor(data.iloc[:, :-1].values, dtype=torch.float32)
    labels = torch.tensor(data.iloc[:, -1].values, dtype=torch.float32).unsqueeze(1)

    dataset = TensorDataset(inputs, labels)
    train_loader = DataLoader(dataset, batch_size=64, shuffle=True)

    model = FraudDetectionModel(input_size=inputs.shape[1])
    trainer = ModelTrainer(model)
    trainer.train(train_loader, epochs=10)
