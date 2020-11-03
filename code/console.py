import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

artist_repository.delete_all()
album_repository.delete_all()

artist1 = Artist("Pink", "Floyd")
artist_repository.save(artist1)

album1 = Album("The Wall", "Rock", artist1)
album_repository.save(album1)





pdb.set_trace