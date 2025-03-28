class Client:
    def __init__(self, client_id, nume, cnp):
        self.__client_id = client_id
        self.__nume = nume
        self.__cnp = cnp

    def get_id(self):
        return self.__client_id

    def get_nume(self):
        return self.__nume

    def get_cnp(self):
        return self.__cnp

    def set_id(self, id):
        self.__client_id = id

    def set_nume(self, nume):
        self.__nume = nume

    def set_cnp(self, cnp):
        self.__cnp = cnp

    def __str__(self):
        return f"{self.__client_id} {self.__nume} {self.__cnp}"

# CNP mai mic = persoană mai bătrână ( < )
    def __lt__(self, other):
        if isinstance(other, Client):
            return self.__cnp < other.__cnp
        raise TypeError("Eroare de validare a cnp-ului!")

# CNP mai mare = persoană mai tânără ( > )
    def __gt__(self, other):
        if isinstance(other, Client):
            return self.__cnp > other.__cnp
        raise TypeError("Eroare de validare a cnp-ului!")


