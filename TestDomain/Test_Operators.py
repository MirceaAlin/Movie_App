from Domain.client import Client
from Domain.movie import Movie

def test_client_operators():
    client1 = Client(1, "Mircea Alin", "5050871813483")
    client2 = Client(2, "Padurar Andra", "5050871813483")
    client3 = Client(2, "Padurar Andra", "6050873210987")
    client4 = Client(1, "Mircea Alin", "6050873210987")

    assert client1 == client2, "Testul pentru egalitate a eșuat"
    assert client1 != client3, "Testul pentru inegalitate a eșuat"
    assert client1 < client3, "Testul pentru 'mai mic' a eșuat"
    assert client4 > client2, "Testul pentru 'mai mare' a eșuat"

def test_movie_operators():
    movie1 = Movie(1, "Inception", "Descriere Inception", "Action")
    movie2 = Movie(2, "Scar Face", "Descriere Scar Face", "Drama")
    movie3 = Movie(2, "Scar Face", "Descriere Scar Face", "Action")

    assert movie1 <= movie2, "Testul pentru 'mai mic sau egal' a eșuat"
    assert movie2 >= movie1, "Testul pentru 'mai mare sau egal' a eșuat"

    combined_movie = movie1 + movie3
    assert combined_movie.get_titlu() == "Inception & Scar Face", "Testul pentru adunare a eșuat (titlu)"
    assert combined_movie.get_descriere() == "Descriere Inception Descriere Scar Face", "Testul pentru adunare a eșuat (descriere)"
    assert combined_movie.get_gen() == "Action", "Testul pentru adunare a eșuat (gen)"

    movie1 += movie3
    assert movie1.get_titlu() == "Inception & Scar Face", "Testul pentru adunare in-place a eșuat (titlu)"
    assert movie1.get_descriere() == "Descriere Inception Descriere Scar Face", "Testul pentru adunare in-place a eșuat (descriere)"
    assert movie1.get_gen() == "Action", "Testul pentru adunare in-place a eșuat (gen)"
