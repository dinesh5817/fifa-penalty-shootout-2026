import random
import time

from team_data import teams
from opponent_selection import choose_opponent
from team_selection import choose_user_team


def shootout():
    """Run a simple penalty shootout game."""

    print("\n===== SHOOTOUT =====")

    user_team = choose_user_team()
    opp_team = choose_opponent(user_team)
    time.sleep(1)

    print("Here are the two teams for the penalty shootout!")
    print(f"It's the penalty shootout in a tense match between {user_team} and {opp_team}!")
    print()
    print("Who is gonna win at this stage? This is the million dollar question here in MetLife Stadium!")

    user_attackers = teams[user_team]["attackers"]
    user_keeper = teams[user_team]["goalkeeper"]
    opp_attackers = teams[opp_team]["attackers"]
    opp_keeper = teams[opp_team]["goalkeeper"]

    print(f"\n⚽ Match: {user_team} vs {opp_team}")
    print(f"{opp_keeper} is the goalkeeper for {opp_team}.")
    print(f"{user_keeper} is the goalkeeper for {user_team}.")

    print("\nBest of 5 penalties.")
    print("You shoot first every round.\n")

    directions = ["L", "C", "R"]
    user_goals = 0
    opp_goals = 0

    time.sleep(1)

    for round_num in range(5):
        print(f"\n========== ROUND {round_num + 1} ==========")

        # === USER SHOOTS ===
        shooter = user_attackers[round_num]
        print(f"\n⚽ {shooter} steps up to take the penalty!")

        while True:
            user_shot = input("Shoot (L/C/R): ").upper().strip()
            if user_shot in directions:
                break
            print("❌ Invalid direction. Please choose L, C, or R.")

        # AI decides dive direction (FIXED)
        ai_dive = random.choice(directions)

        if ai_dive == "C":
            ai_dive_label = "CENTER"
        elif ai_dive == "L":
            ai_dive_label = "LEFT"
        else:
            ai_dive_label = "RIGHT"

        print(f"{opp_keeper} dives {ai_dive_label}...")
        time.sleep(0.8)

        if ai_dive_label == user_shot:
            print("🧤 SAVED!")
            time.sleep(1.5)
            print(f"{opp_keeper} saves the penalty from {shooter}!")
        else:
            print("🥅 GOOOOAAALLL!!")
            print(f"🥅 {shooter} SCORES!")
            if user_goals == 0:
                print(f"It's the first goal for {user_team} scored by {shooter}!")
            else:
                print(f"It's another goal for {user_team}!")

            if shooter == "Cristiano Ronaldo":
                print("SIIUUUUUU! Whoa!")

            user_goals += 1

        print(f"\nScore: {user_team} {user_goals} - {opp_goals} {opp_team}")
        time.sleep(3)

        # === OPPONENT SHOOTS ===
        ai_shooter = opp_attackers[round_num]
        print(f"\n⚽ {ai_shooter} is taking the penalty!")

        while True:
            user_dive = input("Dive (L/C/R): ").upper().strip()
            if user_dive in directions:
                break
            print("❌ Invalid direction. Please choose L, C, or R.")

        ai_shot = random.choice(directions)
        print(f"{ai_shooter} shoots {ai_shot}...")
        time.sleep(0.8)

        if ai_shot == user_dive:
            print("🧤 SAVED!")
            time.sleep(1.5)
            print(f"{user_keeper} saves the penalty from {ai_shooter}!")
        else:
            print(f"🥅 {ai_shooter} SCORES!")
            if opp_goals == 0:
                print(f"It's the first goal for {opp_team} scored by {ai_shooter}!")
            else:
                print(f"It's another goal for {opp_team}!")

            if ai_shooter == "Cristiano Ronaldo":
                print("SIIUUUUUU! Whoa!")

            opp_goals += 1

        print(f"\nScore: {user_team} {user_goals} - {opp_goals} {opp_team}")
        time.sleep(2)

    # === FINAL RESULT ===
    time.sleep(2)
    print("\n" + "="*42)
    print("🏆 PENALTY SHOOTOUT OVER 🏆")
    print("="*42)

    print(f"\nFinal Score: {user_team} {user_goals} - {opp_goals} {opp_team}")

    if user_goals > opp_goals:
        print(f"\n🎉 {user_team} wins the shootout!")
    elif opp_goals > user_goals:
        print(f"\n🏆 {opp_team} wins the shootout!")
        if (opp_goals - user_goals) == 1:
            print("The match was tight until the very end!")
    else:
        print("\n🤝 It's a draw! Sudden death can be added later.")

    # === Special Ronaldo vs Messi Ending ===
    if {user_team, opp_team} == {"Argentina", "Portugal"}:
        if (user_team == "Argentina" and user_goals > opp_goals) or \
           (user_team == "Portugal" and opp_goals > user_goals):
            print("\nUnbelievable! Lionel Messi's Argentina beats Cristiano Ronaldo's Portugal in a classic clash.")
        else:
            print("\nWhat a match! Cristiano Ronaldo is SIUUU-ing in the USA. A game nobody will forget!")

    print("\nThanks for playing!")