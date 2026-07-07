import random
import time

from team_data import teams
from groups import get_team_ranking
from team_selection import choose_user_team
from opponent_selection import choose_opponent


def get_penalty_success_probability(attacker_rank, keeper_rank):
    rating_diff = attacker_rank - keeper_rank
    prob = 0.58 + (rating_diff / 1600)
    return max(0.45, min(0.90, prob))


def shootout(user_team=None, opp_team=None):
    """Run a probability-based penalty shootout game."""

    # === Handle Quick Match Mode ===
    if user_team is None or opp_team is None:
        print("\n===== QUICK MATCH SHOOTOUT =====")
        user_team = choose_user_team()
        opp_team = choose_opponent(user_team)

    print("\n===== SHOOTOUT =====")
    time.sleep(1)

    print("Here are the two teams for the penalty shootout!")
    print(f"It's the penalty shootout in a tense match between {user_team} and {opp_team}!")

    user_attackers = teams[user_team]["attackers"]
    user_keeper = teams[user_team]["goalkeeper"]
    opp_attackers = teams[opp_team]["attackers"]
    opp_keeper = teams[opp_team]["goalkeeper"]

    print(f"\n⚽ Match: {user_team} vs {opp_team}")
    print(f"{opp_keeper} is the goalkeeper for {opp_team}.")
    print(f"{user_keeper} is the goalkeeper for {user_team}.")

    print("\nBest of 5 penalties.\n")

    directions = ["L", "C", "R"]
    user_goals = 0
    opp_goals = 0

    for round_num in range(5):
        print(f"\n========== ROUND {round_num + 1} ==========")

        # USER SHOOTS
        shooter = user_attackers[round_num]
        print(f"\n⚽ {shooter} steps up to take the penalty!")

        while True:
            user_shot = input("Shoot (L/C/R): ").upper().strip()
            if user_shot in directions:
                break
            print("❌ Invalid direction. Please choose L, C, or R.")

        attacker_rank = get_team_ranking(user_team)
        keeper_rank = get_team_ranking(opp_team)
        score_prob = get_penalty_success_probability(attacker_rank, keeper_rank)

        print(f"{opp_keeper} dives...")
        time.sleep(0.8)

        if random.random() < score_prob:
            print("🥅 GOOOOAAALLL!!")
            print(f"🥅 {shooter} SCORES!")
            if shooter == "Cristiano Ronaldo":
                print("SIIUUUUUU! Whoa!")
            user_goals += 1
        else:
            print("🧤 SAVED!")
            time.sleep(1.5)
            print(f"{opp_keeper} saves the penalty from {shooter}!")

        print(f"\nScore: {user_team} {user_goals} - {opp_goals} {opp_team}")
        time.sleep(2)

        # OPPONENT SHOOTS
        ai_shooter = opp_attackers[round_num]
        print(f"\n⚽ {ai_shooter} is taking the penalty!")

        while True:
            user_dive = input("Dive (L/C/R): ").upper().strip()
            if user_dive in directions:
                break
            print("❌ Invalid direction. Please choose L, C, or R.")

        attacker_rank = get_team_ranking(opp_team)
        keeper_rank = get_team_ranking(user_team)
        opp_score_prob = get_penalty_success_probability(attacker_rank, keeper_rank)

        print(f"{ai_shooter} shoots...")
        time.sleep(0.8)

        if random.random() < opp_score_prob:
            print(f"🥅 {ai_shooter} SCORES!")
            if ai_shooter == "Cristiano Ronaldo":
                print("SIIUUUUUU! Whoa!")
            opp_goals += 1
        else:
            print("🧤 SAVED!")
            time.sleep(1.5)
            print(f"{user_keeper} saves the penalty from {ai_shooter}!")

        print(f"\nScore: {user_team} {user_goals} - {opp_goals} {opp_team}")
        time.sleep(2)

    # FINAL RESULT
    time.sleep(2)
    print("\n" + "="*42)
    print("🏆 PENALTY SHOOTOUT OVER 🏆")
    print("="*42)
    print(f"\nFinal Score: {user_team} {user_goals} - {opp_goals} {opp_team}")

    if user_goals > opp_goals:
        print(f"\n🎉 {user_team} wins the shootout!")
    elif opp_goals > user_goals:
        print(f"\n🏆 {opp_team} wins the shootout!")
    else:
        print("\n🤝 It's a draw!")

    if user_goals > opp_goals:
        winner = user_team
        loser = opp_team
        draw = False
    elif opp_goals > user_goals:
        winner = opp_team
        loser = user_team
        draw = False
    else:
        winner = None
        loser = None
        draw = True

    return {
        "winner": winner,
        "loser": loser,
        "draw": draw,
        "goal_difference": abs(user_goals - opp_goals)
    }