from Repository.movie_repository import MovieRepo
from Repository.client_repository import ClientRepo
from Service.client_service import ClientService
from Service.movie_service import MovieService
from UI.ui import Console

if __name__ == '__main__':
    client_repo = ClientRepo()
    movie_repo = MovieRepo()
    client_service = ClientService(client_repo)
    movie_service = MovieService(movie_repo)
    console = Console()
    console.run()
