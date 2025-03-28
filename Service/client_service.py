from Domain.client import Client
from Repository.client_repository import ClientRepo


class ClientService:
    def __init__(self, client_repo):
        self.client_repo = client_repo

    def adaugare_client(self, client):
        self.client_repo.adaugare_client(client)

    def get_clienti(self):
        return self.client_repo.get_clienti()

    def stergere_client(self, client_id):
        self.client_repo.stergere_client(client_id)

    def modificare_client(self, client_id, nume=None, cnp=None):
        self.client_repo.modificare_client(client_id, nume, cnp)
