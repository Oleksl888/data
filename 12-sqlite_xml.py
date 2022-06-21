import xml.etree.ElementTree as ET
import sqlite3


#Function for extracting music data
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None


#Create a database file
db_connect = sqlite3.connect('music_1.sqlite3')
db = db_connect.cursor()
#OPTIONALLY delete previous tables in database
db.execute("DROP TABLE IF EXISTS Artist")
db.execute("DROP TABLE IF EXISTS Genre")
db.execute("DROP TABLE IF EXISTS Album")
db.execute("DROP TABLE IF EXISTS Track")
#Create Tables in database as per template
db.execute('''CREATE TABLE Artist (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
name TEXT UNIQUE);''')
db.execute('''CREATE TABLE Genre (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
name TEXT UNIQUE);''')
db.execute('''CREATE TABLE Album (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
artist_id INTEGER, title TEXT UNIQUE);''')
db.execute('''CREATE TABLE Track (
id INTEGER NOT NULL PRIMARY KEY
AUTOINCREMENT UNIQUE,
title TEXT UNIQUE,
album_id INTEGER,
genre_id INTEGER,
len INTEGER, rating INTEGER, count INTEGER);''')
db_connect.commit()
#Open the xml file and find the necessary data
contents = ET.parse('Library.xml')
music_list = contents.findall('dict/dict/dict')
#Loop through the list to find all the music data and add it to the database
print(len(music_list))
for i in music_list:
    if lookup(i, 'Track ID') is None:
        continue
    artist_name = lookup(i, 'Artist')
    genre = lookup(i, 'Genre')
    album = lookup(i, 'Album')
    track_name = lookup(i, 'Name')
    track_length = lookup(i, 'Total Time')
    track_rating = lookup(i, 'Rating')
    track_count = lookup(i, 'Play Count')
    if artist_name is None or track_name is None or album is None:
        continue
    db.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist_name, ))
    db.execute("SELECT id FROM Artist WHERE name=?", (artist_name, ))
    artist_id = db.fetchone()[0]
    if genre is None:
        try:
            db.execute('INSERT INTO Genre (name) VALUES ("No Name")')
            genre_id = db.lastrowid
        except:
            db.execute("SELECT id FROM Genre WHERE name='No Name'")
            genre_id = db.fetchone()[0]
    else:
        try:
            db.execute('INSERT INTO Genre (name) VALUES (?)', (genre, ))
            genre_id = db.lastrowid
        except:
            db.execute("SELECT id FROM Genre WHERE name=?", (genre, ))
            genre_id = db.fetchone()[0]
    db.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)', (album, artist_id))
    db.execute('SELECT id FROM Album WHERE title=?', (album, ))
    album_id = db.fetchone()[0]
    db.execute('''INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count)
    VALUES (?, ?, ?, ?, ?, ?)''',
               (track_name, album_id, genre_id, track_length, track_rating, track_count))
    db_connect.commit()
db_connect.close()
