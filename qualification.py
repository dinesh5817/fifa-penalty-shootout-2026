
def qualified_teams(sorted_teams):
    """Returns the top 32 teams from the final standings"""
    qualified = []
    for team, stats in sorted_teams[:32]:   # Take top 32 teams
        qualified.append(team)
    return qualified