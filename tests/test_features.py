from world_cup_2026_ai_quant.features import goal_difference, match_result, points_for_result


def test_goal_difference():
    assert goal_difference(2, 1) == 1


def test_match_result():
    assert match_result(1, 1) == "draw"
    assert match_result(0, 2) == "away_win"


def test_points_for_result():
    assert points_for_result("home_win") == (3, 0)
