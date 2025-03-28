from Domain.client import Client
from Domain.movie import Movie
from Repository.client_repository import ClientRepo
from Repository.movie_repository import MovieRepo


def test_adaugare_client_repo():
    repo = ClientRepo()
    client = Client(1, 'Alexandra', 6030127890123)

    repo.adaugare_client(client)

    clienti = repo.get_clienti()
    assert len(clienti) == 1
    assert clienti[0].get_nume() == 'Alexandra'
    assert clienti[0].get_cnp() == 6030127890123


def test_stergere_client_repo():
    repo = ClientRepo()
    client1 = Client(1, 'Alexandra', 6030127890123)
    client2 = Client(2, 'Andrei', 5012345678901)

    repo.adaugare_client(client1)
    repo.adaugare_client(client2)

    repo.stergere_client(1)

    clienti = repo.get_clienti()
    assert len(clienti) == 1
    assert clienti[0].get_id() == 2


def test_modificare_client_repo():
    repo = ClientRepo()
    client = Client(1, 'Alexandra', 6030127890123)

    repo.adaugare_client(client)
    repo.modificare_client(1, 'Ioana', 6045678901234)

    clienti = repo.get_clienti()
    assert len(clienti) == 1
    assert clienti[0].get_nume() == 'Ioana'
    assert clienti[0].get_cnp() == 6045678901234


def test_adaugare_movie_repo():
    repo = MovieRepo()
    movie = Movie(1, 'We live in time', 'Love story', 'romance')

    repo.adaugare_movie(movie)

    movies = repo.get_movies()
    assert len(movies) == 1
    assert movies[0].get_id() == 1
    assert movies[0].get_titlu() == 'We live in time'
    assert movies[0].get_descriere() == 'Love story'
    assert movies[0].get_gen() == 'romance'


def test_stergere_movie_repo():
    repo = MovieRepo()
    movie1 = Movie(1, 'It ends with us', 'love story', 'drama')
    movie2 = Movie(2, 'Divergent', 'survival story', 'action')

    repo.adaugare_movie(movie1)
    repo.adaugare_movie(movie2)

    repo.stergere_movie(1)

    movies = repo.get_movies()
    assert len(movies) == 1
    assert movies[0].get_id() == 2


def test_modificare_movie_repo():
    repo = MovieRepo()
    movie = Movie(1, 'Don t move', 'children s fear', 'thriller')

    repo.adaugare_movie(movie)
    repo.modificare_movie(1, 'The idea of you', 'love story', 'romance')

    movies = repo.get_movies()
    assert len(movies) == 1
    assert movies[0].get_titlu() == 'The idea of you'
    assert movies[0].get_descriere() == 'love story'
    assert movies[0].get_gen() == 'romance'


if __name__ == '__main__':
    test_modificare_client_repo()
    test_stergere_client_repo()
    test_adaugare_client_repo()
    test_adaugare_movie_repo()
    test_stergere_movie_repo()
    test_modificare_movie_repo()
