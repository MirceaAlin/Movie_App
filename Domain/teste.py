from Domain.movie import Movie
from Domain.client import Client


def test_movie():
    movie = Movie(1, 'We live in time', 'romantic story', 'romance')

    assert movie.get_id() == 1
    assert movie.get_titlu() == 'We live in time'
    assert movie.get_descriere() == 'romantic story'
    assert movie.get_gen() == 'romance'

    movie.set_titlu('Divergent')
    movie.set_gen('action')
    movie.set_descriere('survival story')

    assert movie.get_titlu() == 'Divergent'
    assert movie.get_descriere() == 'survival story'
    assert movie.get_gen() == 'action'


def test_client():
    client = Client(1, 'Maria', 6050501543234)

    assert client.get_id() == 1
    assert client.get_nume() == 'Maria'
    assert client.get_cnp() == 6050501543234

    client.set_cnp(6050501543566)
    client.set_nume('Ana')

    assert client.get_nume() == 'Ana'
    assert client.get_cnp() == 6050501543566


if __name__ == '__main__':
    test_client()
    test_movie()
