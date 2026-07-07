from game_sim import simulate_match
from shootout import shootout
import time


def run_full_knockouts(qualified_teams, user_team):
    """Runs the full knockout stage and returns only the champion"""
    teams = qualified_teams.copy()

    # Round of 32
    teams = play_knockout_round(teams, user_team, "ROUND OF 32", 16)

    # Round of 16
    teams = play_knockout_round(teams, user_team, "ROUND OF 16", 8)

    # Quarter-finals
    teams = play_knockout_round(teams, user_team, "QUARTER-FINALS", 4)

    # Semi-finals
    teams = play_knockout_round(teams, user_team, "SEMI-FINALS", 2)

    # Final
    champion_list = play_knockout_round(teams, user_team, "FINAL", 1)
    champion = champion_list[0]

    return champion


def play_knockout_round(teams, user_team, round_name, num_matches):
    next_round = []
    print(f"\n========== {round_name} ==========")

    for i in range(num_matches):
        home = teams[i]
        away = teams[-(i + 1)]

        print(f"\n{home} vs {away}")

        if home == user_team or away == user_team:
            print(f"\nITS {user_team.capitalize()}'s MATCH NOW!")
            time.sleep(1)

            if user_team == home:
                result = shootout(user_team, away)
            else:
                result = shootout(user_team, home)

            time.sleep(1)

            if result.get("draw"):
                print("It's a draw! (Home team advances for now)")
                winner = home
            else:
                winner = result.get("winner", home)

            print(f"→ {winner} advances!")
            next_round.append(winner)

        else:
            result = simulate_match(home, away)
            time.sleep(1)

            if result.get("draw"):
                print("It's a draw! (Home team advances for now)")
                winner = home
            else:
                winner = result.get("winner", home)

            print(f"→ {winner} advances!")
            next_round.append(winner)

    return next_round