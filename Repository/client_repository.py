from Domain.client import Client


class ClientRepo:
    def __init__(self):
        self.__clienti = []

    def adaugare_client(self, client):
        """
        Este creat un obiect de tip client si este adaugat la lista de clienti.
        :param client:
        :return:
        """
        client = Client(client.get_id(), client.get_nume(), client.get_cnp())
        self.__clienti.append(client)

    def get_clienti(self):
        """
        Functia pentru a accesa lista de clienti.
        :return:
        """
        return self.__clienti

    def stergere_client(self, client_id):
        """
        Functia pentru stergerea unui client dupa id.
        :param client_id:
        :return:
        """
        for client in self.__clienti:
            if client.get_id() == client_id:
                self.__clienti.remove(client)
                break

    def modificare_client(self, client_id, nume, cnp):
        """
        Functia pentru modificarea clientului.
        :param client_id:
        :param nume:
        :param cnp:
        :return:
        """
        for client in self.__clienti:
            if client.get_id() == client_id:
                if nume is not None:
                    client.set_nume(nume)
                if cnp is not None:
                    client.set_cnp(cnp)
                break

