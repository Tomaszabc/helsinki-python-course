import json

class HockeyStatistics:
    def __init__(self):
        self.players = []

    def read_file(self, filename: str):
        with open(filename, 'r') as file:
            self.players = json.load(file)
        print(f"read the data of {len(self.players)} players")

    def search_player(self, name: str):
        for player in self.players:
            if player["name"].lower() == name.lower():
                self.print_player(player)
                return
        print("Player not found")

    def print_player(self, player):
        name = player["name"]
        team = player["team"]
        goals = player["goals"]
        assists = player["assists"]
        points = goals + assists
        print(f"{name:21}{team:3} {goals:3} + {assists:2} = {points:3}")


    def list_teams(self):
        teams = sorted(set(player["team"] for player in self.players))
        for team in teams:
            print(team)

    def list_countries(self):
        countries = sorted(set(player["nationality"] for player in self.players))
        for country in countries:
            print(country)

    def players_in_team(self, team: str):
        found = False
        for player in sorted(self.players, key=lambda p: p["goals"] + p["assists"], reverse=True):
            if player["team"].upper() == team.upper():
                self.print_player(player)
                found = True
        if not found:
            print(f"No players found in team {team}")

    def players_from_country(self, country: str):
        found = False
        for player in sorted(self.players, key=lambda p: p["goals"] + p["assists"], reverse=True):
            if player["nationality"].upper() == country.upper():
                self.print_player(player)
                found = True
        if not found:
            print(f"No players from {country}")

    def most_points(self, n: int):
        sorted_players = sorted(self.players, key=lambda p: (p["goals"] + p["assists"], p["goals"]), reverse=True)
        for player in sorted_players[:n]:
            self.print_player(player)

    def most_goals(self, n: int):
        sorted_players = sorted(self.players, key=lambda p: (p["goals"], -p["games"]), reverse=True)
        for player in sorted_players[:n]:
            self.print_player(player)

    def run(self):
        filename = input("file name: ")
        self.read_file(filename)

        while True:
            print("\ncommands:")
            print("0 quit")
            print("1 search for player")
            print("2 teams")
            print("3 countries")
            print("4 players in team")
            print("5 players from country")
            print("6 most points")
            print("7 most goals")

            command = input("command: ")

            if command == "0":
                break
            elif command == "1":
                name = input("name: ")
                self.search_player(name)
            elif command == "2":
                self.list_teams()
            elif command == "3":
                self.list_countries()
            elif command == "4":
                team = input("team: ")
                self.players_in_team(team)
            elif command == "5":
                country = input("country: ")
                self.players_from_country(country)
            elif command == "6":
                n = int(input("how many: "))
                self.most_points(n)
            elif command == "7":
                n = int(input("how many: "))
                self.most_goals(n)

app = HockeyStatistics()
app.run()