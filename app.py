import constants

teams = constants.TEAMS [::]
players = constants.PLAYERS [::]
length_of_teams = len(teams)
num_of_players = len(players) 
players_per_team =  num_of_players_per_team = num_of_players / length_of_teams
teams_with_players = {}

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
user_option_choice = input('Enter and option --> ')
try:
  if user_option_choice == 1:
      team_index = 0  
      num = 0 
  for player in players:
    print(player)
    if(len(teams_with_players[teams[team_index]]) != 6):
          curr_team = teams_with_players[teams[team_index]]
          print(curr_team)
          pritn(teams_with_players)
    elif user_option_choice == 2:
          print('Good Bye')
             
except ValueError:
    break
  

  if __name__ == "__main__":
      print(players[0])
teams_with_players[teams[team_index]['name']]