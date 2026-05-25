import sqlite3

DATABASE = 'hockey.db'

with sqlite3.connect(DATABASE) as db:

    cursor = db.cursor()
    show_all_players = 'SELECT * FROM players;'
    cursor.execute(show_all_players)
    results = cursor.fetchall()
    print(results)
    # Print the data so you can actually see it
    for player in results:
        print(f"Player: {player[1]} Team: {player[2]}")

with sqlite3.connect(DATABASE) as db:

    cursor = db.cursor()
    top20 = 'SELECT * FROM players ORDER BY points DESC LIMIT 20;'
    cursor.execute(top20)
    results = cursor.fetchall()
    print(results)
    # Print the data so you can actually see it
    for top_20 in results:
        print(f"Player: {player[1]}, Team: {player[2]}, Points: {player[8]}")
        print('hello')
