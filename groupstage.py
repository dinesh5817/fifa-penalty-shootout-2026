from groups import groups
from shootout import shootout
from game_sim import simulate_match
from standings import update_standings, initialize_standings, print_standings
import time
from qualification import qualified_teams


GROUP_FIXTURES = (
    ((0, 1), (2, 3)),   # Matchday 1
    ((0, 2), (1, 3)),   # Matchday 2
    ((0, 3), (1, 2))    # Matchday 3
)


def play_group_stage(user_team):
    initialize_standings()
    print("\n========== GROUP STAGE ==========")

    for matchday_no, matchday in enumerate(GROUP_FIXTURES, start=1):
        print(f"\n========== MATCHDAY {matchday_no} ==========")

        for group_name, group in groups.items():
            print(f"\nGroup {group_name}")
            team_list = list(group)

            for home_index, away_index in matchday:
                home = team_list[home_index]
                away = team_list[away_index]

                print(f"{home} vs {away}")

                if user_team == home or user_team == away:
                    time.sleep(2)
                    print(f"\nIt's your turn! You are playing as {user_team}.")
                    time.sleep(2)
                    print(f"\nITS {user_team.capitalize()}'s MATCH NOW!")

                    if user_team == home:
                        result = shootout(user_team, away)
                    else:
                        result = shootout(user_team, home)

                    time.sleep(2)
                    update_standings(result, home=home, away=away)

                else:
                    result = simulate_match(home, away)
                    time.sleep(1)
                    update_standings(result, home=home, away=away)

    print("\n========== FINAL GROUP STANDINGS ==========")
    sorted_teams = print_standings()

    # Get qualified teams
    top_32 = qualified_teams(sorted_teams)
    print("\n✅ Top 32 teams qualified for Round of 32:")
    print(top_32)

    return top_32