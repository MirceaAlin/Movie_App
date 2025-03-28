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

# ( + ) pentru filmele cu același gen
    def __add__(self, other):
        if isinstance(other, Movie):
            if self.__gen == other.__gen:
                new_titlu = self.__titlu + " & " + other.__titlu
                new_descriere = self.__descriere + " " + other.__descriere
                return Movie(0, new_titlu, new_descriere, self.__gen)
            else:
                raise ValueError("Filmele trebuie să aibă același gen pentru a fi combinate.")

# ( += )
    def __iadd__(self, other):
        if isinstance(other, Movie):
            if self.__gen == other.__gen:
                self.__titlu += " & " + other.__titlu
                self.__descriere += " " + other.__descriere
                return self
            else:
                raise ValueError("Filmele trebuie să aibă același gen pentru a putea fi combinate.")
