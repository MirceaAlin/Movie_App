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


def teste_operator_lt():
    client1 = Client(1, "Ion", 1900101123456)
    client2 = Client(2, "Maria", 2000101123456)
    client3 = Client(3, "Vasile", 1900101123456)
    client4 = Client(4, "Elena", 2000201123456)

    assert client1 < client2
    assert not (client2 < client1)
    assert not (client1 < client3)
    assert client2 < client4


def teste_operator_gt():
    client1 = Client(1, "Ion", 1900101123456)
    client2 = Client(2, "Maria", 2000101123456)
    client3 = Client(3, "Vasile", 1900101123456)
    client4 = Client(4, "Elena", 2000201123456)

    assert client2 > client1
    assert not (client1 > client2)
    assert not (client1 > client3)
    assert client4 > client2


if __name__ == '__main__':
    test_client()
    test_movie()
    teste_operator_lt()
    teste_operator_gt()
    print("Teste trecute cu succes!")
