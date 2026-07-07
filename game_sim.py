import random
from groups import get_team_ranking

def simulate_match(home, away):
    home_rank = get_team_ranking(home)      # Get FIFA points of home team
    away_rank = get_team_ranking(away)      # Get FIFA points of away team

    rating_diff = home_rank - away_rank     # How much stronger is home team?

    # Step 1: Calculate win probability for the home team
    base_prob = 0.5 + (rating_diff / 1800)

    # Step 2: Make sure probability stays between 15% and 85%
    win_prob = max(0.15, min(0.93, base_prob))
    
    draw_prob = 0.28
    loss_prob = 1 - win_prob - draw_prob

    # Step 3: Randomly decide the result based on probabilities
    result_type = random.choices(
        ["home_win", "draw", "away_win"],
        weights=[win_prob, draw_prob, loss_prob]
    )[0]

    # Step 4: Generate scores based on result
    if result_type == "home_win":
        home_score = random.randint(1, 4)
        away_score = random.randint(0, home_score - 1)
        winner = home
        loser = away
        draw = False

    elif result_type == "away_win":
        away_score = random.randint(1, 4)
        home_score = random.randint(0, away_score - 1)
        winner = away
        loser = home
        draw = False

    else:  # Draw
        home_score = random.randint(0, 3)
        away_score = home_score
        winner = None
        loser = None
        draw = True

    goal_difference = abs(home_score - away_score)

    print(f"Match Result: {home} {home_score} - {away_score} {away}")

    return {
        "home": home,
        "away": away,
        "winner": winner,
        "loser": loser,
        "draw": draw,
        "goal_difference": goal_difference
    }