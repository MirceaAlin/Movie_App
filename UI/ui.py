from Domain.client import Client
from Domain.movie import Movie
from Repository.client_repository import ClientRepo
from Repository.movie_repository import MovieRepo
from Service.client_service import ClientService
from Service.movie_service import MovieService


class Console:
    def __init__(self):
        client_repo = ClientRepo()
        movie_repo = MovieRepo()
        self.client_service = ClientService(client_repo)
        self.movie_service = MovieService(movie_repo)

    def afisare_meniu_principal(self):
        print("Închiriere Filme\n"
              "1. Adaugare film\n"
              "2. Adaugare client\n"
              "3. Stergere film\n"
              "4. Stergere client\n"
              "5. Modificare film\n"
              "6. Modificare client\n"
              "7. Afisare filme\n"
              "8. Afisare clienti\n"
              "9. Comparare clienti\n"
              "0. Exit")

    def run(self):
        while True:
            self.afisare_meniu_principal()
            choice = input("Alegeti o optiune: ")

            if choice == "1":
                self.ui_adaugare_movie()
            elif choice == "2":
                self.ui_adaugare_client()
            elif choice == "3":
                self.ui_stergere_movie()
            elif choice == "4":
                self.ui_stergere_client()
            elif choice == "5":
                self.ui_modificare_movie()
            elif choice == "6":
                self.ui_modificare_client()
            elif choice == "7":
                self.ui_afisare_filme()
            elif choice == "8":
                self.ui_afisare_clienti()
            elif choice == "9":
                self.ui_comparare_clienti()
            elif choice == "0":
                break
            else:
                print("Optiune invalida.")

    def ui_adaugare_movie(self):
        try:
            movie_id = int(input("Introduceti id-ul filmului: "))
            if any(movie.get_id() == movie_id for movie in self.movie_service.get_movies()):
                print("Eroare: Un film cu acest ID exista deja.")
                return

            titlu = input("Introduceti titlul filmului: ")
            descriere = input("Introduceti descrierea filmului: ")
            gen = input("Introduceti genul filmului: ")
            self.movie_service.adaugare_movie(Movie(movie_id, titlu, descriere, gen))
            print("Film adaugat cu succes!")
        except ValueError:
            print("Eroare: ID-ul filmului trebuie sa fie un numar intreg.")
        except Exception as e:
            print(f"Eroare la adaugarea filmului: {e}")

    def ui_adaugare_client(self):
        try:
            client_id = int(input("Introduceti id-ul clientului: "))
            if any(client.get_id() == client_id for client in self.client_service.get_clienti()):
                print("Eroare: Un client cu acest ID exista deja.")
                return

            nume = input("Introduceti numele clientului: ")
            cnp = input("Introduceti cnp-ul clientului: ")
            client = Client(client_id, nume, cnp)
            self.client_service.adaugare_client(client)
            print("Client adaugat cu succes!")
        except ValueError:
            print("Eroare: ID-ul clientului trebuie sa fie un numar intreg.")
        except Exception as e:
            print(f"Eroare la adaugarea clientului: {e}")

    def ui_stergere_movie(self):
        try:
            filme = self.movie_service.get_movies()
            if not filme:
                print("Nu exista filme disponibile pentru a fi sterse.")
                return

            movie_id = int(input("Introduceti id-ul filmului pe care doriti sa-l stergeti: "))
            if not any(movie.get_id() == movie_id for movie in filme):
                print("Eroare: Nu exista un film cu acest ID.")
                return

            self.movie_service.stergere_movie(movie_id)
            print("Film sters cu succes!")
        except ValueError:
            print("Eroare: ID-ul filmului trebuie sa fie un numar intreg.")
        except Exception as e:
            print(f"Eroare la stergerea filmului: {e}")

    def ui_stergere_client(self):
        try:
            clienti = self.client_service.get_clienti()
            if not clienti:
                print("Nu exista clienti disponibili pentru a fi stersi.")
                return

            client_id = int(input("Introduceti id-ul clientului pe care doriti sa-l stergeti: "))
            if not any(client.get_id() == client_id for client in clienti):
                print("Eroare: Nu exista un client cu acest ID.")
                return

            self.client_service.stergere_client(client_id)
            print("Client sters cu succes!")
        except ValueError:
            print("Eroare: ID-ul clientului trebuie sa fie un numar intreg.")
        except Exception as e:
            print(f"Eroare la stergerea clientului: {e}")

    def ui_modificare_movie(self):
        try:
            movie_id = int(input("Introduceti id-ul filmului pe care doriti sa-l modificati: "))
            if not any(movie.get_id() == movie_id for movie in self.movie_service.get_movies()):
                print("Eroare: Nu exista un film cu acest ID.")
                return

            titlu = input("Introduceti noul titlu al filmului: ")
            descriere = input("Introduceti noua descriere a filmului: ")
            gen = input("Introduceti noul gen al filmului: ")
            self.movie_service.modificare_movie(movie_id, titlu, descriere, gen)
            print("Film actualizat cu succes!")
        except ValueError:
            print("Eroare: ID-ul filmului trebuie sa fie un numar intreg.")
        except Exception as e:
            print(f"Eroare la modificarea filmului: {e}")

    def ui_modificare_client(self):
        try:
            client_id = int(input("Introduceti id-ul clientului pe care doriti sa-l modificati: "))
            if not any(client.get_id() == client_id for client in self.client_service.get_clienti()):
                print("Eroare: Nu exista un client cu acest ID.")
                return

            nume = input("Introduceti noul nume al clientului (sau lasati gol pentru a nu-l schimba): ")
            cnp = input("Introduceti noul cnp al clientului (sau lasati gol pentru a nu-l schimba): ")
            self.client_service.modificare_client(client_id, nume if nume else None, cnp if cnp else None)
            print("Client actualizat cu succes!")
        except ValueError:
            print("Eroare: ID-ul clientului trebuie sa fie un numar intreg.")
        except Exception as e:
            print(f"Eroare la modificarea clientului: {e}")

    def ui_afisare_filme(self):
        try:
            filme = self.movie_service.get_movies()
            if not filme:
                print("Nu exista filme in acest moment.")
            else:
                print("Filme:")
                for movie in filme:
                    print(f"Id film: {movie.get_id()}")
                    print(f"Titlu film: {movie.get_titlu()}")
                    print(f"Descriere film: {movie.get_descriere()}")
                    print(f"Gen film: {movie.get_gen()}")
        except Exception as e:
            print(f"Eroare la afisarea filmelor: {e}")

    def ui_afisare_clienti(self):
        try:
            clienti = self.client_service.get_clienti()
            if not clienti:
                print("Nu exista clienti in acest moment.")
            else:
                print("Clienti:")
                for client in clienti:
                    print(f"Id client: {client.get_id()}")
                    print(f"Nume client: {client.get_nume()}")
                    print(f"cnp client: {client.get_cnp()}")
        except Exception as e:
            print(f"Eroare la afisarea clientilor: {e}")

    def cauta_client_dupa_id(self, client_id):
        for client in self.client_service.get_clienti():
            if client.get_id() == client_id:
                return client
        return None

    def ui_comparare_clienti(self):
        try:
            client_id_1 = int(input("Introduceti ID-ul primului client: "))
            client_id_2 = int(input("Introduceti ID-ul celui de-al doilea client: "))

            client1 = self.cauta_client_dupa_id(client_id_1)
            client2 = self.cauta_client_dupa_id(client_id_2)

            if client1 is None:
                print(f"Eroare: Nu exista un client cu ID-ul {client_id_1}.")
                return
            if client2 is None:
                print(f"Eroare: Nu exista un client cu ID-ul {client_id_2}.")
                return

            cnp1 = client1.get_cnp()
            cnp2 = client2.get_cnp()

            # print(f"Client 1: {client1.get_nume()} (CNP: {cnp1})")
            # print(f"Client 2: {client2.get_nume()} (CNP: {cnp2})")

            if cnp1 < cnp2:
                print(f"{client1.get_nume()} este mai in varsta decat {client2.get_nume()}.")
            elif cnp1 > cnp2:
                print(f"{client2.get_nume()} este mai in varsta decat {client1.get_nume()}.")
            else:
                print(f"Ambii clienti au acelasi CNP, deci sunt de aceeasi varsta.")
        except ValueError:
            print("Eroare: ID-ul clientului trebuie sa fie un numar intreg.")
        except Exception as e:
            print(f"Eroare la compararea varstei clientilor: {e}")


if __name__ == "__main__":
    console = Console()
    console.run()
