from Domain.movie import Movie


class MovieRepo:
    def __init__(self):
        self.__movies = []

    def adaugare_movie(self, movie):
        """

        :param movie: Este creat un obiect de tip movie si este adaugat la lista de filme.
        :return:
        """
        movie = Movie(movie.get_id(), movie.get_titlu(), movie.get_descriere(), movie.get_gen())
        self.__movies.append(movie)

    def get_movies(self):
        """
        Functia pentru a accesa lista de filme.
        :return:
        """
        return self.__movies

    def stergere_movie(self, movie_id):
        """
        Functia pentru stergerea filmului dupa id.
        :param movie_id:
        :return:
        """
        for movie in self.__movies:
            if movie.get_id() == movie_id:
                self.__movies.remove(movie)
                break

    def modificare_movie(self, movie_id, titlu, descriere, gen):
        """
        Functia pentru a face update unui film.
        :param movie_id:
        :param titlu:
        :param descriere:
        :param gen:
        :return:
        """
        for movie in self.__movies:
            if movie.get_id() == movie_id:
                if titlu is not None:
                    movie.set_titlu(titlu)
                if descriere is not None:
                    movie.set_descriere(descriere)
                if gen is not None:
                    movie.set_gen(gen)
                break
