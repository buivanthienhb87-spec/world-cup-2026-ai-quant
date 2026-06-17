from world_cup_2026_ai_quant.models import MatchPrediction
from world_cup_2026_ai_quant.export import export_predictions
import json, tempfile, os

def test_export():
    preds = [MatchPrediction("A", "B", 0.5, 0.3, 0.2)]
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        export_predictions(preds, f.name)
        path = f.name
    data = json.loads(open(path, encoding="utf-8").read())
    os.unlink(path)
    assert data[0]["home_team"] == "A"
