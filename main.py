from Repository.movie_repository import MovieRepo
from Repository.client_repository import ClientRepo
from Service.client_service import ClientService
from Service.movie_service import MovieService
from TestDomain.Test_Operators import test_movie_operators, test_client_operators
from UI.ui import Console

if __name__ == '__main__':
    test_client_operators()
    test_movie_operators()
    client_repo = ClientRepo()
    movie_repo = MovieRepo()
    client_service = ClientService(client_repo)
    movie_service = MovieService(movie_repo)
    console = Console()
    console.run()
