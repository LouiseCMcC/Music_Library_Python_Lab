from optparse import Values
from ssl import VERIFY_X509_PARTIAL_CHAIN
from db.run_sql import run_sql
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