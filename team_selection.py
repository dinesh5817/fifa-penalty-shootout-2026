from team_data import teams


def choose_user_team():
    """Ask for a valid team until the user enters one."""

    while True:
        team = input("Choose your country: ").title().strip()

        if team in teams:
            return team

        print("❌ Invalid team. Please choose one of the 48 World Cup teams.")
