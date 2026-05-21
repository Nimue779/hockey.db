import sqlite3

db = sqlite3.connect('hockey.db')
cursor = db.cursor()
show_all_players = 'SELECT * FROM players;'

db.close()
