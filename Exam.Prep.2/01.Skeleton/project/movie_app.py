from project.movie_specification.fantasy import Fantasy
from project.movie_specification.action import Action
from project.movie_specification.thriller import Thriller
from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        for user in self.users_collection:
            if username == user.username:
                raise Exception("User already exists!")

        current_user = User(username, age)
        self.users_collection.append(current_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):

        for user in self.users_collection:
            if username == user.username:
                break

        else:
            raise Exception("This user does not exist!")

        if not username == movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if not username == movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key, value in kwargs.items():
            if key == "title":
                movie.title = value
            if key == "year":
                movie.year = value
            if key == "age_restriction":
                movie.age_restriction = value
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if not username == movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)

        for user in self.users_collection:
            if username == user.username:
                user.movies_owned.remove(movie)
                return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        if username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        for user in self.users_collection:
            if username == user.username:
                if movie in user.movies_liked:
                    raise Exception(f"{username} already liked the movie {movie.title}!")

                user.movies_liked.append(movie)

        movie.likes += 1
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        for user in self.users_collection:
            if username == user.username:
                if movie not in user.movies_liked:
                    raise Exception(f"{username} has not liked the movie {movie.title}!")

                user.movies_liked.remove(movie)
        movie.likes -= 1
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        sorted_collection = self.movies_collection.copy()
        sorted_collection.sort(key=lambda movie: (-movie.year, movie.title))

        result = []
        for movie in sorted_collection:
            result.append(movie.details())

        return "\n".join(result)

    def __str__(self):
        users = []
        movies = []
        final_result = ""
        if self.users_collection:
            for user in self.users_collection:
                users.append(user.username)
            result = ", ".join(users)
            final_result = f"All users: {result}"

        else:
            final_result = "All users: No users."

        if self.movies_collection:
            for movie in self.movies_collection:
                movies.append(movie.title)
            result = ", ".join(movies)
            final_result += f"\nAll movies: {result}"

        else:
            final_result += "\nAll movies: No movies."

        return final_result
