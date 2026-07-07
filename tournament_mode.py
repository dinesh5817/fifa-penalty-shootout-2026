from team_selection import choose_user_team
from groupstage import play_group_stage


def tournament():
    """Show the tournament placeholder message."""

    user_team = choose_user_team()
    print("\n===== TOURNAMENT =====")
    print(f"You have chosen {user_team} for the FIFA World Cup.")
    play_group_stage(user_team)
