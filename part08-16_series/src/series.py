class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons  
        self.genres = genres
        self.ratings = []

    def rate(self, rating:int):
        self.ratings.append(rating)

    def __str__(self):
        genre_string = ", ".join(self.genres)

        if len(self.ratings) == 0:
            return f"{self.title} ({self.seasons} seasons) \ngenres: {genre_string} \nno ratings"
        else:
            number = len(self.ratings)
            average = sum(self.ratings) / number
            return f"{self.title} ({self.seasons} seasons) \ngenres: {genre_string} \n{number} ratings, average {average:.1f} points"


dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
dexter.rate(4)
dexter.rate(5)
dexter.rate(5)
dexter.rate(3)
dexter.rate(0)
print(dexter)