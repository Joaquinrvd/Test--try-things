
#this is a test not the real assinment


import random  # Import the random module

# Create a list of players stored in the players variable
players = ["Devon", "Kauri", "Isaiah",
           "Braylen", "Taymur", "Xavier",
           "Avery", "Taqari", "Kenlon",
           "Marshawn", "Nahum", "Kamari",
           "Kristopher", "Joseph", "Darren", 
           "Carl", "Walter", "Jeffrey", 
           "Nishad", "Maximus", "Ja’Den", 
           "Jarmauri", "Eustace", "Semaj", "Joaquin"]

def pick_teams(players):
    random.shuffle(players)  # Shuffle the list of players
    half = len(players) // 2
    team1 = players[:half]         # First half of players
    team2 = players[half:]         # Second half of players

    team_caption1 = random.choice(team1)  # Randomly assign a team captain from team 1
    team_caption2 = random.choice(team2)  # Randomly assign a team captain from team 2

    print("\nTeam 1:")
    print("Captain:", team_caption1)
    for player in team1:
        print("-", player)

    print("\nTeam 2:")
    print("Captain:", team_caption2)
    for player in team2:
        print("-", player)

# Loop until user is satisfied with teams
while True:
    pick_teams(players)
    user_input = input("\nAre you happy with these teams? (yes/no): ").strip().lower()
    if user_input == "yes":
        print("Great! Teams are set.")
        break
    else:
        print("\nShuffling teams again...\n")
