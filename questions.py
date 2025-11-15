import random
from cs50 import SQL

# initialize database
db = SQL("sqlite:///statistics.db")
league_names = ["Premier League", "Serie A", "LaLiga", "Bundesliga"]
competition_names = [
    "Premier League",
    "Serie A",
    "LaLiga",
    "Bundesliga",
    "Champions League",
    "Club World Cup",
    "Community Shield",
    "FA Cup",
    "UEFA Super Cup",
    "Nedbank Cup",
]


# Player Profiles
# Based on which team a player picks, return a list of all players in the team
def main(): ...


def random_question():
    functions = [trivia_2, trivia_4, trivia_5, trivia_6, trivia_7]
    random.shuffle(functions)
    random_function = functions[0]

    if random_function == trivia_7:
        player, trivia = random_function(random.choice(league_names))
    else:
        player, trivia = random_function(random.choice(competition_names))

    answer, question = "", ""
    possible_answers = []
    for ans, quest in trivia.items():
        answer = ans
        question = quest

    if random_function == trivia_7:
        for i in range(4):
            possible_answers.append(player[i]["season_manager_manager_name"])
    else:
        for i in range(4):
            possible_answers.append(player[i]["player_slug"])

    random.shuffle(possible_answers)
    return (question, answer, possible_answers)


def bestOf():
    functions = [
        bestOf_trivia_1,
        bestOf_trivia_2,
        bestOf_trivia_3,
        bestOf_trivia_4,
        bestOf_trivia_5,
    ]
    random.shuffle(functions)
    random_function = functions[0]
    team, trivia = random_function(random.choice(league_names))

    answer, question = "", ""
    possible_answers = []
    for ans, quest in trivia.items():
        answer = ans
        question = quest

    for i in range(4):
        possible_answers.append(team[i]["team_name"])

    random.shuffle(possible_answers)
    return (question, answer, possible_answers)


# Ask a list of trivia questions based on the selected team players picking a random player everytime
def trivia_1(team_name):

    team_player = db.execute(
        "SELECT player_slug,"
        " player_id,"
        " country_of_birth,"
        " main_position,"
        " current_club_name,"
        " foot, contract_expires, joined"
        " FROM player_profiles, team_details"
        " WHERE player_profiles.current_club_id = team_details.club_id"
        " AND current_club_name = ?",
        team_name,
    )
    if not team_player:
        raise ValueError
    else:
        random.shuffle(team_player)

    player_performance = db.execute(
        "SELECT player_slug,"
        " season_name,"
        " player_performances.competition_name,"
        " team_name,"
        " goals,"
        " assists,"
        " own_goals,"
        " penalty_goals"
        " FROM player_profiles, team_details, player_performances"
        " WHERE player_profiles.current_club_id = team_details.club_id"
        " AND player_performances.player_id = player_profiles.player_id"
        " AND player_performances.player_id = ?"
        " AND player_performances.team_name = ?",
        team_player[0]["player_id"],
        team_name,
    )
    if player_performance:
        # create big dictionary of question: answer elements
        trivia = [
            {
                team_player[0][
                    "country_of_birth"
                ]: f"Which country does {team_player[0]["player_slug"]} come from? "
            },
            {
                team_player[0][
                    "foot"
                ]: f"What is {team_player[0]["player_slug"]}’s preferred foot? "
            },
            {
                team_player[0][
                    "main_position"
                ]: f"What position does {team_player[0]["player_slug"]} play? "
            },
            {
                player_performance[0][
                    "goals"
                ]: f"How many goals did {player_performance[0]["player_slug"]} score in the {player_performance[0]["season_name"]} season {player_performance[0]["competition_name"]}?: "
            },
            {
                player_performance[0][
                    "assists"
                ]: f"How many assists did {player_performance[0]["player_slug"]} have in {player_performance[0]["season_name"]} for the {player_performance[0]["competition_name"]}?: "
            },
            {
                player_performance[0][
                    "own_goals"
                ]: f"How many own goals did {player_performance[0]["player_slug"]} score in the {player_performance[0]["season_name"]} season for the {player_performance[0]["competition_name"]}?: "
            },
            {
                player_performance[0][
                    "penalty_goals"
                ]: f"How many penalty goals did {player_performance[0]["player_slug"]} score in the {player_performance[0]["season_name"]} season for the {player_performance[0]["competition_name"]}?: "
            },
        ]

        random.shuffle(trivia)
        return trivia[0]
    else:
        return trivia_1(team_name)


def trivia_2(competition_name):
    player = db.execute(
        "SELECT player_slug,"
        " season_name, competition_name, "
        "team_name, goals, "
        "assists, penalty_goals "
        "FROM player_profiles, "
        "player_performances "
        "WHERE player_profiles.player_id = player_performances.player_id "
        "AND player_performances.competition_name = ? "
        "ORDER BY CAST(goals AS INTEGER) DESC LIMIT 500",
        competition_name,
    )

    random.shuffle(player)
    return [
        player,
        {
            player[0][
                "player_slug"
            ]: f"In {player[0]['competition_name']} {player[0]["season_name"]} season I scored {player[0]["goals"]} overall goals, with {player[0]["penalty_goals"]} penalty goals and {player[0]["assists"]} assists for {player[0]["team_name"]}. Who am I?"
        },
    ]


def trivia_4(competition_name):
    season = db.execute("SELECT season_name FROM player_performances LIMIT 500")
    random.shuffle(season)
    player = db.execute(
        "SELECT player_slug,"
        " season_name, competition_name, "
        "team_name, goals, "
        "assists, penalty_goals "
        "FROM player_profiles, "
        "player_performances "
        "WHERE player_profiles.player_id = player_performances.player_id "
        "AND competition_name = ? "
        "AND season_name = ?"
        "ORDER BY CAST(goals AS INTEGER) DESC LIMIT 5",
        competition_name,
        season[0]["season_name"],
    )
    if player:
        return [
            player,
            {
                player[0][
                    "player_slug"
                ]: f"I was the top goal scorer in {player[0]["competition_name"]} (season {player[0]["season_name"]}) with {player[0]["goals"]} goals. I played for {player[0]["team_name"]} at the time. Who am I?"
            },
        ]
    else:
        return trivia_4(competition_name)


def trivia_5(competition_name):
    season = db.execute("SELECT season_name FROM player_performances LIMIT 500")
    random.shuffle(season)
    player = db.execute(
        "SELECT player_slug,"
        " season_name, competition_name, "
        "team_name, goals, "
        "assists, penalty_goals "
        "FROM player_profiles, "
        "player_performances "
        "WHERE player_profiles.player_id = player_performances.player_id "
        "AND competition_name = ? "
        "AND season_name = ?"
        "ORDER BY CAST(assists AS INTEGER) DESC LIMIT 5",
        competition_name,
        season[0]["season_name"],
    )
    if player:
        return [
            player,
            {
                player[0][
                    "player_slug"
                ]: f"I had the most assists in {player[0]["competition_name"]} (season {player[0]["season_name"]}) with {player[0]["assists"]} assists. I played for {player[0]["team_name"]} at the time. Who am I?"
            },
        ]
    else:
        return trivia_5(competition_name)


def trivia_6(competition_name):
    season = db.execute("SELECT season_name FROM player_performances LIMIT 500")
    random.shuffle(season)
    player = db.execute(
        "SELECT player_slug,"
        " season_name, competition_name, "
        "team_name, goals, "
        "assists, penalty_goals "
        "FROM player_profiles, "
        "player_performances "
        "WHERE player_profiles.player_id = player_performances.player_id "
        "AND competition_name = ?"
        "AND season_name = ?"
        "ORDER BY CAST(penalty_goals AS INTEGER) DESC LIMIT 5",
        competition_name,
        season[0]["season_name"],
    )

    if player:
        return [
            player,
            {
                player[0][
                    "player_slug"
                ]: f"I had the most penalty goals in {player[0]["competition_name"]} (season {player[0]["season_name"]}) with {player[0]["penalty_goals"]} goals. I played for {player[0]["team_name"]} at the time. Who am I?"
            },
        ]
    else:
        return trivia_6(competition_name)


def trivia_7(competition_name):
    season = db.execute("SELECT season_name FROM player_performances LIMIT 500")
    random.shuffle(season)
    player = db.execute(
        "SELECT competition_name, "
        "season_manager_manager_name, "
        "season_rank, season_season, "
        "season_points, season_goals_for, "
        "team_name "
        "FROM team_competitions_seasons "
        "WHERE season_league_league_name = ? "
        "AND season_season = ? "
        "ORDER BY CAST(season_rank AS INTEGER) ASC LIMIT 10",
        competition_name,
        season[0]["season_name"],
    )
    if player:
        return [
            player,
            {
                player[0][
                    "season_manager_manager_name"
                ]: f"I was the club manager for {player[0]["team_name"]} in {player[0]["competition_name"]} (season {player[0]["season_season"]}) which ranked 1st place. My team also finished the season with a total of {player[0]["season_goals_for"]} goals. Who am I?"
            },
        ]
    else:
        return trivia_7(competition_name)


def bestOf_trivia_1(competition_name):
    season = db.execute("SELECT season_season FROM team_competitions_seasons LIMIT 100")
    random.shuffle(season)
    team = db.execute(
        "SELECT competition_name, "
        "season_manager_manager_name, "
        "season_rank, season_season, "
        "season_points, season_goals_for, "
        "season_goal_difference, "
        "season_losses, "
        "season_wins, "
        "team_name "
        "FROM team_competitions_seasons "
        "WHERE season_league_league_name = ? "
        "AND season_season = ? "
        "ORDER BY CAST(season_rank AS INTEGER) ASC LIMIT 10",
        competition_name,
        season[0]["season_season"],
    )

    if team:
        return [
            team,
            {
                team[0][
                    "team_name"
                ]: f"Which team won the {team[0]["competition_name"]} title ( season: {team[0]["season_season"]} ) with {team[0]["season_goals_for"]} goals and {team[0]["season_wins"]} wins ?"
            },
        ]
    else:
        return bestOf_trivia_1(competition_name)


def bestOf_trivia_2(competition_name):
    season = db.execute("SELECT season_season FROM team_competitions_seasons LIMIT 100")
    random.shuffle(season)
    team = db.execute(
        "SELECT competition_name, "
        "season_manager_manager_name, "
        "season_rank, season_season, "
        "season_points, season_goals_for, "
        "season_goal_difference, "
        "season_losses, "
        "season_wins, "
        "team_name "
        "FROM team_competitions_seasons "
        "WHERE season_league_league_name = ? "
        "AND season_season = ? "
        "ORDER BY CAST(season_rank AS INTEGER) DESC LIMIT 20",
        competition_name,
        season[0]["season_season"],
    )

    if team:
        return [
            team,
            {
                team[0][
                    "team_name"
                ]: f"Which team came in last place in {team[0]["competition_name"]} ( season: {team[0]["season_season"]} ) with only {team[0]["season_wins"]} wins and {team[0]["season_goals_for"]} goals ?"
            },
        ]
    else:
        return bestOf_trivia_2(competition_name)


def bestOf_trivia_3(competition_name):
    season = db.execute("SELECT season_season FROM team_competitions_seasons LIMIT 100")
    random.shuffle(season)
    team = db.execute(
        "SELECT competition_name, "
        "season_manager_manager_name, "
        "season_rank, season_season, "
        "season_points, season_goals_for, "
        "season_goal_difference, "
        "season_losses, "
        "season_wins, "
        "team_name "
        "FROM team_competitions_seasons "
        "WHERE season_league_league_name = ? "
        "AND season_season = ? "
        "ORDER BY CAST(season_goals_for AS INTEGER) DESC LIMIT 10",
        competition_name,
        season[0]["season_season"],
    )

    if team:
        return [
            team,
            {
                team[0][
                    "team_name"
                ]: f"Which team had the most goals in {team[0]["competition_name"]} ( season: {team[0]["season_season"]} ) with {team[0]["season_goals_for"]} goals ?"
            },
        ]
    else:
        return bestOf_trivia_3(competition_name)


def bestOf_trivia_4(competition_name):
    team = db.execute(
        "SELECT team_name, COUNT(*) AS 'titles' "
        "FROM team_competitions_seasons "
        "WHERE season_league_league_name = ? "
        "AND season_rank = 1 "
        "GROUP BY ( team_name) ORDER BY COUNT(*) DESC",
        competition_name,
    )

    if team:
        return [
            team,
            {
                team[0][
                    "team_name"
                ]: f"Which team holds the most title wins in the {competition_name} with {team[0]["titles"]} titles ?"
            },
        ]
    else:
        return bestOf_trivia_4(competition_name)


def bestOf_trivia_5(competition_name):
    team = db.execute(
        "SELECT team_name, season_losses "
        "FROM team_competitions_seasons "
        "WHERE season_league_league_name = ? "
        "ORDER BY CAST ( season_losses AS INTEGER ) DESC LIMIT 10",
        competition_name,
    )

    if team:
        return [
            team,
            {
                team[0][
                    "team_name"
                ]: f"Which team had the most losses in {competition_name} with {team[0]["season_losses"]} losses ?"
            },
        ]
    else:
        return bestOf_trivia_5(competition_name)


if __name__ == "__main__":
    main()
