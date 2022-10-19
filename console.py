import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()

artist1= Artist('Elvis Presley')
artist_repository.save(artist1)

artist2= Artist('Korn')
artist_repository.save(artist2)

album1= Album('Elvis Christmas album', 'Rock and Roll', artist1)
album_repository.save(album1)
album2= Album('Girls! Girls! Girls!', 'Rock and Roll', artist1)
album_repository.save(album2)
album3= Album('The Nothng', 'Nu Metal', artist2)
album_repository.save(album3)
album4= Album('Requiem', "Nu Metal", artist2)
album_repository.save(album4)

artist_repository.select_all()
album_repository.select_all()
