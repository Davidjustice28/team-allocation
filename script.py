from random import choice,shuffle


def pick_teams(choices,num):
    while True:
        teams = [] 
        players = choices.copy()
        amount_of_teams = num
        num_of_players = len(players) /amount_of_teams
        shuffle(choices)
        while len(teams) < num:
            team = players[:int(num_of_players)]
            teams.append(team)
            for p in team:
                players.remove(p)
        
        for t in teams:
            team_num = teams.index(t)+ 1
            team_captain = choice(t)
            print(f"Team {team_num} captain is {team_captain}")
            for p in t:
                print(p)
            print("\n")

        response = input("Pick teams again? y or n: ")

        if response == 'n':
            return teams
        else:
            teams.clear()
            print("\nRecalculating teams...\n")
        
names = ["david", "james", "katelyn", "brandon", "sam", "bernard", "sharon", "mark", "bryant", "kelly", "anthony", "dennis"]

print("\nWelcome to Team Allocator!\n")

playing_teams = pick_teams(names,3)
startingTeam = choice(playing_teams)

print(f"Team {playing_teams.index(startingTeam) +1} goes first")