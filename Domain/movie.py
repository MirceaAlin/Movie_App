class Movie:
    def __init__(self, movie_id, titlu, descriere, gen):
        self.__movie_id = movie_id
        self.__titlu = titlu
        self.__descriere = descriere
        self.__gen = gen

    def get_id(self):
        return self.__movie_id

    def get_titlu(self):
        return self.__titlu

    def get_descriere(self):
        return self.__descriere

    def get_gen(self):
        return self.__gen

    def set_movie_id(self, movie_id):
        self.__movie_id = movie_id

    def set_titlu(self, titlu):
        self.__titlu = titlu

    def set_descriere(self, descriere):
        self.__descriere = descriere

    def set_gen(self, gen):
        self.__gen = gen

    def __str__(self):
        return f"{self.__movie_id} {self.__titlu} {self.__descriere} {self.__gen}"
