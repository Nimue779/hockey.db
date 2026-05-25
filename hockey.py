import sqlite3

DATABASE = 'hockey.db'

print('Welcome to my Hockey Database')
print('1. Print all player and their team')
print('2. Print all players alphabetically and their stats')
print('3. Print top 20 players')
# this query prints all players and their team, no extra stats
with sqlite3.connect(DATABASE) as db:

    cursor = db.cursor()
    show_all_players = 'SELECT * FROM players;'
    cursor.execute(show_all_players)
    results = cursor.fetchall()
    print(results)
    # Print the data so you can actually see it
    for player in results:
        print(f"Player: {player[1]} Team: {player[2]}")

# this query shows the top 20 players in the league based on their points
with sqlite3.connect(DATABASE) as db:

    cursor = db.cursor()
    top20 = 'SELECT * FROM players ORDER BY points DESC LIMIT 20;'
    cursor.execute(top20)
    results = cursor.fetchall()
    print(results)
    # Print the data so you can actually see it
    for player in results:
        print(f"Player: {player[1]}, Team: {player[2]}, Points: {player[8]}")

# this query will print all players alphabetically. this includes player,
# team, what hand they shoot with,
# position, games played, points, the +/-/ and penalty minutes
with sqlite3.connect(DATABASE) as db:

    cursor = db.cursor()
    alphabetical = 'SELECT * FROM players ORDER BY name ASC;'
    cursor.execute(alphabetical)
    results = cursor.fetchall()
    print(results)
    # Print the data so you can actually see it
    for player in results:
        print(f"Player: {player[1]}, Team: {player[2]}, Shoots: {player[3]},\
Position: {player[4]}, Games played: {player[5]},\
Points: {player[8]},+/-: {player[9]}, Penalty Minutes: {player[10]}")
