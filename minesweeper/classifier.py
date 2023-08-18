import torch.nn as nn
import torch


class Classifer(nn.Module):

    def forward(self, x):
        return self.model(x)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.model = nn.Sequential(
            nn.Conv2d(1, 64, 4, 2, 1),
            nn.LazyBatchNorm2d(),
            nn.LeakyReLU(0.2),
            nn.Dropout2d(),

            nn.Conv2d(64, 128, 4, 2, 1),
            nn.LazyBatchNorm2d(),
            nn.LeakyReLU(0.2),
            nn.Dropout2d(),

            nn.Flatten(),

            nn.LazyLinear(1024),
            nn.LazyBatchNorm1d(),
            nn.LeakyReLU(0.2),

            nn.LazyLinear(13),
            nn.Sigmoid(),
        )

    def predict(self, x: torch.Tensor):
        y = self.forward(x)
        return torch.argmax(y, dim=x.dim() - 3)
