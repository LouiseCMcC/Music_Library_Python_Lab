from db.run_sql import run_sql
from models.album import Album
from models.artist import Artist
import album_repository

def save(artist):
    sql= 'INSERT INTO artist (name)VALUES(%s)RETURNING *'
    values = [artist.name]
    result = run_sql(sql, values)
    id = result[0]['id']
    artist.id = id
    return artist

def select(id):
    sql = 'SELECT * FROM albums WHERE id=%s'
    values= [id]
    results = run_sql(sql, values)
    if results:
        result= results[0]
        artist= Artist(result['name'], result['id'])
    return artist

def update(artist):
    sql= 'UPDATE artist SET (name) VALUES (%s) WHERE id=%s'
    values = [artist['name'],artist['id']]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM artist WHERE id = %s" 
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql= 'DELETE FROM artist'
    run_sql(sql)