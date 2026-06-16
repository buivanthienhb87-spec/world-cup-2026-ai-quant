from __future__ import annotations

from dataclasses import dataclass
from math import log
from typing import Iterable, Sequence


@dataclass(frozen=True)
class BinaryMetrics:
    accuracy: float
    log_loss: float
    brier_score: float


def evaluate_binary(y_true: Sequence[int], y_prob: Sequence[float]) -> BinaryMetrics:
    if len(y_true) != len(y_prob):
        raise ValueError("y_true and y_prob must have the same length")
    if not y_true:
        raise ValueError("at least one observation is required")

    eps = 1e-15
    correct = 0
    log_loss_total = 0.0
    brier_total = 0.0

    for actual, prob in zip(y_true, y_prob):
        clipped = min(max(float(prob), eps), 1 - eps)
        predicted = 1 if clipped >= 0.5 else 0
        correct += int(predicted == int(actual))
        log_loss_total += -(actual * log(clipped) + (1 - actual) * log(1 - clipped))
        brier_total += (clipped - actual) ** 2

    n = len(y_true)
    return BinaryMetrics(
        accuracy=correct / n,
        log_loss=log_loss_total / n,
        brier_score=brier_total / n,
    )
