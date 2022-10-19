from db.run_sql import run_sql
from models.artist import Artist


def save(artist):
    sql= 'INSERT INTO artists (name) VALUES (%s) RETURNING *'
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

def select_all():
    artists = []
    sql= 'SELECT * FROM artists'
    results = run_sql(sql)

    for row in results:
        artist=Artist(row['name'])
        artists.append(artist)
    return artists

def update(artist):
    sql= 'UPDATE artists SET (name) VALUES (%s) WHERE id=%s'
    values = [artist['name'],artist['id']]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM artists WHERE id = %s" 
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql= 'DELETE FROM artists'
    run_sql(sql)