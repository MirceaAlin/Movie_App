from Repository.movie_repository import MovieRepo
from Domain.movie import Movie


class MovieService:
    def __init__(self, movie_repo):
        self.movie_repo = movie_repo

    def adaugare_movie(self, movie):
        self.movie_repo.adaugare_movie(movie)

    def stergere_movie(self, movie_id):
        self.movie_repo.stergere_movie(movie_id)

    def modificare_movie(self, movie_id, titlu=None, descriere=None, gen=None):
        self.movie_repo.modificare_movie(movie_id, titlu, descriere, gen)

    def get_movies(self):
        return self.movie_repo.get_movies()
