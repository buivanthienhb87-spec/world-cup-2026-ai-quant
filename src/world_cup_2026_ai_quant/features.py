from __future__ import annotations


def goal_difference(home_goals: int, away_goals: int) -> int:
    return int(home_goals) - int(away_goals)


def match_result(home_goals: int, away_goals: int) -> str:
    diff = goal_difference(home_goals, away_goals)
    if diff > 0:
        return "home_win"
    if diff < 0:
        return "away_win"
    return "draw"


def points_for_result(result: str) -> tuple[int, int]:
    if result == "home_win":
        return 3, 0
    if result == "away_win":
        return 0, 3
    if result == "draw":
        return 1, 1
    raise ValueError(f"unknown result: {result}")
