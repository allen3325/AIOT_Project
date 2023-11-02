import torch
from torch import nn


class SentClassifier(nn.Module):
    def __init__(self, input_dim, n_classes):
        super(SentClassifier, self).__init__()

        # dimensionality
        self.input_dim = input_dim
        self.n_classes = n_classes
        self.hidden_dim = 500

        # creates a MLP
        self.classifier = nn.Sequential(
            nn.Linear(self.input_dim, self.hidden_dim),
            nn.ReLU(),  # 使用 ReLU activation function
            nn.Linear(self.hidden_dim, self.n_classes))

    def forward(self, sentence_vec, target=None):

        res = ''

        predicted = self.classifier(sentence_vec)  # use classifier to predicted
        # [0.111, 1.111] -> [a, b]信心分數 -> 取大，可以知道為哪一類 -> predicted_class 就是大的 index
        predicted_value, predicted_class = torch.max(predicted, 1)

        if predicted_class == 0:
            res = 'positive'
        else:
            res = 'negative'


        # print(f"predicted: {predicted}")
        # print(f"predicted_value: {predicted_value}")

        if target is not None:  # 有解答
            criterion = nn.CrossEntropyLoss()
            loss = criterion(predicted, target)
            return predicted_class, loss
        else:  # 沒解答
            return predicted, res
