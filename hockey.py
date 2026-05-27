# imports
import sqlite3

# constants and variables
DATABASE = 'hockey.db'


# functions
#prints all players and team
def print_all_players():
    '''print all players nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM players'
    cursor.execute(sql)
    results = cursor.fetchall()
    print('All players and teams')
    # loop through the results
    for player in results:
        print(f"Player:{player[1]:<30} Team:{player[2]}")
    # loop finishes here
    db.close()


# allows users to type in a specific team
def print_all_players_in_team():
    '''print all players from chosen team nicely'''
    user_input = input("Enter team abbreviation\n")

    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = f"SELECT * FROM players WHERE team LIKE '%{user_input}%'"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f'All players from {user_input}')
    # loop through the results
    for player in results:
        print(f"Player:{player[1]} Team:{player[2]}")
    # loop finishes here
    db.close()

# allows users to search for specific players
def print_specific_players_stats():
    '''print a player that the uses has input and their season stats'''
    user_input = input("Enter player name\n")

    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = f"SELECT name, team, points FROM players WHERE name LIKE '%{user_input}%'"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f'Print players with names matching {user_input}')
    # loop through the results
    for player in results:
        print(f"Player:{player[0]} Team:{player[1]} Points:{player[2]}")
    # loop finishes here
    db.close()

def top20():
    '''print top 20 players'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT name, team, points FROM players ORDER BY points DESC LIMIT 20'
    cursor.execute(sql)
    results = cursor.fetchall()
    print('Top 20 players by points')
    # loop through the results
    for player in results:
        print(f"Player:{player[0]:<30} Team:{player[1]} Points:{player[2]}")
    # loop finishes here
    db.close()

# main code
while True:
    user_input = input("\nWhat would you like to do?\n1Print all players \n2Choose a team\n3Choose players\n4Print top 20 players\n")

    if user_input == '1':
        print_all_players()
    elif user_input == '2':
        print_all_players_in_team()
    elif user_input == '3':
        print_specific_players_stats()
    elif user_input == '4':
        top20()
    else:
        print('end')
        break
        
