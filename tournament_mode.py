from team_selection import choose_user_team
from groupstage import play_group_stage


from knockouts import run_full_knockouts

def tournament():
    user_team = choose_user_team()

    print("\n===== TOURNAMENT =====")
    print(f"You have chosen {user_team}")

    qualified = play_group_stage(user_team)

    champion = run_full_knockouts(qualified, user_team)

    print(f"\n🏆 WORLD CHAMPION: {champion}")