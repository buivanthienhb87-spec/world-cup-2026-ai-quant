from world_cup_2026_ai_quant.models import MatchPrediction

def test_most_likely():
    pred = MatchPrediction("Team A", "Team B", 0.5, 0.3, 0.2)
    assert pred.most_likely() == "home_win"

def test_validation():
    valid = MatchPrediction("A", "B", 0.4, 0.3, 0.3)
    invalid = MatchPrediction("A", "B", 0.5, 0.5, 0.5)
    assert valid.is_valid()
    assert not invalid.is_valid()
