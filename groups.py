"""
groups.py
FIFA World Cup 2026 - Actual Groups (Official Draw)
"""

groups = {
    'A': {
        'Mexico': 1642,
        'South Africa': 1445,
        'South Korea': 1530,
        'Czechia': 1480
    },
    'B': {
        'Canada': 1475,
        'Bosnia And Herzegovina': 1460,
        'Qatar': 1390,
        'Switzerland': 1615
    },
    'C': {
        'Brazil': 1785,
        'Morocco': 1670,
        'Haiti': 1280,
        'Scotland': 1455
    },
    'D': {
        'United States': 1628,
        'Paraguay': 1510,
        'Australia': 1468,
        'Turkey': 1550
    },
    'E': {
        'Germany': 1725,
        'Curacao': 1240,
        'Ivory Coast': 1545,
        'Ecuador': 1560
    },
    'F': {
        'Netherlands': 1745,
        'Japan': 1595,
        'Sweden': 1520,
        'Tunisia': 1480
    },
    'G': {
        'Belgium': 1790,
        'Egypt': 1525,
        'Iran': 1495,
        'New Zealand': 1305
    },
    'H': {
        'Spain': 1830,
        'Cape Verde': 1395,
        'Saudi Arabia': 1430,
        'Uruguay': 1640
    },
    'I': {
        'France': 1845,
        'Senegal': 1580,
        'Iraq': 1340,
        'Norway': 1565
    },
    'J': {
        'Argentina': 1886,
        'Austria': 1535,
        'Jordan': 1320,
        'Algeria': 1510
    },
    'K': {
        'Portugal': 1740,
        'Colombia': 1610,
        'Uzbekistan': 1295,
        'Dr Congo': 1485
    },
    'L': {
        'England': 1805,
        'Croatia': 1720,
        'Ghana': 1440,
        'Panama': 1310
    }
}


def get_all_teams():
    """Returns a flat list of all 48 teams"""
    all_teams = []
    for group_teams in groups.values():
        all_teams.extend(group_teams.keys())
    return all_teams


def get_team_ranking(team_name):
    """Returns the FIFA ranking points of a team"""
    for group_teams in groups.values():
        if team_name in group_teams:
            return group_teams[team_name]
    return None