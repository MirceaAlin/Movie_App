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


def teste_operator_eq():
    client1 = Client(1, "Ion", "1234567890123")
    client2 = Client(2, "Maria", "1234567890123")
    client3 = Client(3, "George", "9876543210987")
    client4 = Client(4, "Ana", "9876543210987")

    assert client1 == client2
    assert client3 == client4
    assert not (client1 == client3)
    assert not (client2 == client4)


def teste_operator_ne():
    client1 = Client(1, "Ion", "1234567890123")
    client2 = Client(2, "Maria", "1234567890123")
    client3 = Client(3, "George", "9876543210987")
    client4 = Client(4, "Ana", "9876543210987")

    assert client1 != client3
    assert client2 != client4
    assert not (client1 != client2)
    assert not (client3 != client4)

if __name__ == '__main__':
    test_client()
    test_movie()
    teste_operator_ne()
    teste_operator_eq()
    print("Teste trecute cu succes!")
