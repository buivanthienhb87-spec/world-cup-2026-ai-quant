from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class MatchPrediction:
    home_team: str
    away_team: str
    home_win_prob: float
    draw_prob: float
    away_win_prob: float

    def most_likely(self) -> str:
        probs = {"home_win": self.home_win_prob, "draw": self.draw_prob, "away_win": self.away_win_prob}
        return max(probs, key=probs.get)

    def is_valid(self) -> bool:
        total = self.home_win_prob + self.draw_prob + self.away_win_prob
        return abs(total - 1.0) < 0.01
