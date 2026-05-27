# imports
import sqlite3

# constants and variables
DATABASE = 'hockey.db'


# functions
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

# main code
while True:
    user_input = input("\nWhat would you like to do?\n1Print all players \n2Exit \n")

    if user_input == '1':
        print_all_players()

