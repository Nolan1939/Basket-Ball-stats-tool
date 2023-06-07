import constants

teams = constants.TEAMS [::]
players = constants.PLAYERS [::]
length_of_teams = len(teams)
num_of_players = len(players) 
players_per_team =  num_of_players_per_team = num_of_players / length_of_teams
teams_with_players = {}
team_index = {}

for team in teams:
      teams_with_players[team] = []
        
print('BASKETBALL TEAM STATS TOOL')
print('\n')


while True:  
  print('=====MENU====')
  print('\n')
  print('Here are your choices: ')
  print('1) Display stats')
  print('2) Quit')
  break

while true:
    try:
        user_option_choice = input('Enter and option --> ')
        if user_option_choice == 1:
            print ('\n --Teams--')
        for index, team in enumerate(teams):
            print(str(index + 1) + ')' + str(team))
while true:
    try:      
            get_team_choice = int(input('\nChoose A Team --> '))
        if(not(1 <= get_team_choice <= len(teams))):
            print("Thats not a valid option")
            break    
        print("\nTeam: " + teams[get_team_choice - 1] + 'Stats')
        print("---------------------")
        print("Number of players: " + str(len(teams_with_players[teams[1]])))
        print('\nPlayers On Team: ')
        players_on_team = []    
        for player in teams_with_players[teams[get_team_choice - 1]]
            players_on_team.append(player['name'])
        print(' ' + ','-join(players_on_team))
        print('')
        break
    except ValueError:
    print("Error: Please use numbers only")
elif user_option_choice == 2:
     print("Goodbye")
     break
else:
     print("Thats not a valid choice")
except ValueError:
    print('Error: Please use numbers only\n')
                    

          
        
  

    if __name__ == "__main__":
      print(players[0])
teams_with_players[teams[team_index]['name']]