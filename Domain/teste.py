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


def test_movie_operator_le():
    movie1 = Movie(1, "Titanic", "O poveste dramatica", "Drama")
    movie2 = Movie(2, "Avatar", "Un univers spectaculos", "SF")
    movie3 = Movie(1, "Titanic (alt)", "Altă descriere", "Drama")

    assert movie1 <= movie2
    assert movie1 <= movie3
    assert not (movie2 <= movie1)


def test_movie_operator_ge():
    movie1 = Movie(1, "Titanic", "O poveste dramatica", "Drama")
    movie2 = Movie(2, "Avatar", "Un univers spectaculos", "SF")
    movie3 = Movie(1, "Titanic (alt)", "Altă descriere", "Drama")

    assert movie2 >= movie1
    assert movie3 >= movie1
    assert not (movie1 >= movie2)


if __name__ == '__main__':
    test_client()
    test_movie()
    test_movie_operator_le()
    test_movie_operator_ge()
    print("Teste trecute cu succes!")
