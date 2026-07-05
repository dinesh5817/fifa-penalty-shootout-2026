import random

from team_data import teams


def choose_opponent(user_team):
    """Choose an opponent randomly or manually."""

    while True:
        choice = input(
            "\nOpponent Selection\n"
            "R = Random\n"
            "C = Choose Yourself\n"
            "Enter choice: "
        ).upper().strip()

        if choice == "R":
            available = list(teams.keys())
            available.remove(user_team)
            return random.choice(available)

        if choice == "C":
            while True:
                opponent = input("Choose opponent country: ").title().strip()

                if opponent not in teams:
                    print("❌ Invalid team.")
                    continue

                if opponent == user_team:
                    print("❌ You cannot play against your own team.")
                    continue

                return opponent

        print("❌ Please enter R or C.")
