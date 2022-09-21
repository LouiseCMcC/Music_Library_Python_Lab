from db.run_sql import run_sql
from models import artist
from models.album import Album
from models.artist import Artist
import artist_repository

def save(album):
    sql= 'INSERT INTO albums (title, genre, artist)VALUES(%s, %s, %s)RETURNING *'
    values = [album.title, album.genre, album.artist]
    result = run_sql(sql, values)
    id = result[0]['id']
    album.id = id
    return album

def select_all():
    albums = []
    sql= 'SELECT * FROM albums'

    for row in albums:
        artist = artist_repository.select(row['name'])
        album= Album(album['title'], album['genre'], artist)
        albums.append(album)
    return albums

def select(id):
    sql = 'SELECT * FROM albums WHERE id=%s'
    values= [id]
    results = run_sql(sql, values)
    if results:
        result= results[0]
        artist= artist_repository.select(result['name'])
        album= Album(result['title'], result['genre'], artist, result['id'])
    return album

def update(album):
    sql= 'UPDATE album SET (title, genre, artist) VALUES (%s, %s, %s) WHERE id=%s'
    values = [album['title'], album['genre'], album['artist'], album['id']]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM album WHERE id = %s" 
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql= 'DELETE FROM album'
    run_sql(sql)



