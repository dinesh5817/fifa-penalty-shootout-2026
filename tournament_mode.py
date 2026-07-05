from team_selection import choose_user_team


def tournament():
    """Show the tournament placeholder message."""

    user_team = choose_user_team()
    print("\n===== TOURNAMENT =====")
    print(f"You have chosen {user_team} for the World Cup.")
    print("Tournament mode is under development. Please check back later!")
