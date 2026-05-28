class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons  
        self.genres = genres

    def __str__(self):
        genre_list = self.genres
        genre_string = ", ".join(genre_list)
        return f"{self.title} ({self.seasons} seasons) \ngenres: {genre_string} \nno ratings"

dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
print(dexter)