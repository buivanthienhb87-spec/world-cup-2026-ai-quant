from __future__ import annotations
import json
from pathlib import Path
from .models import MatchPrediction

def export_predictions(predictions: list[MatchPrediction], output_path: str) -> None:
    data = [{"home_team": p.home_team, "away_team": p.away_team, "home_win_prob": p.home_win_prob, "draw_prob": p.draw_prob, "away_win_prob": p.away_win_prob} for p in predictions]
    Path(output_path).write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
