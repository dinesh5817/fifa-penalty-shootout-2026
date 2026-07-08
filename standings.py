# standings.py

standings = {}

def initialize_standings():
    """Initialize standings for all teams"""
    from groups import get_all_teams
    for team in get_all_teams():
        standings[team] = {
            "played": 0,
            "won": 0,
            "drawn": 0,
            "lost": 0,
            "gd": 0,
            "points": 0
        }

def update_standings(result, home=None, away=None):
    """Update standings after a match"""
    
    if result["draw"]:
        # It's a draw
        standings[home]["played"] += 1
        standings[away]["played"] += 1
        standings[home]["drawn"] += 1
        standings[away]["drawn"] += 1
        standings[home]["points"] += 1
        standings[away]["points"] += 1

    else:
        # There is a winner and loser
        winner = result["winner"]
        loser = result["loser"]

        standings[winner]["played"] += 1
        standings[loser]["played"] += 1
        standings[winner]["won"] += 1
        standings[loser]["lost"] += 1
        standings[winner]["points"] += 3

        # Goal difference
        standings[winner]["gd"] += result["goal_difference"]
        standings[loser]["gd"] -= result["goal_difference"]

def print_standings():
    print("\n" + "=" * 90)
    print(f"{'Team':<28} {'Pld':>5} {'W':>4} {'D':>4} {'L':>4} {'GD':>6} {'Pts':>5}")
    print("=" * 90)

    sorted_teams = sorted(
        standings.items(),
        key=lambda x: (x[1]["points"], x[1]["gd"]),
        reverse=True
    )

    for team, stats in sorted_teams:
        print(
            f"{team:<28}"
            f"{stats['played']:>5}"
            f"{stats['won']:>4}"
            f"{stats['drawn']:>4}"
            f"{stats['lost']:>4}"
            f"{stats['gd']:>6}"
            f"{stats['points']:>5}"
        )

    print("=" * 90)

    return sorted_teams