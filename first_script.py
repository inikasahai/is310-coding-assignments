favorite_movies = [
    ("Lights Out", 2016),
    ("Scream", 1996),
    ("Superman", 1978),
    ("Inside Out", 2015),
    ("Zootopia 2", 2025)
]

def check_movie(movie):
    title, year = movie
    
    if year < 2000:
        print(f"{title}: This movie was released before 2000")
        return None
    else:
        print(f"{title}: This movie was released after 2000")
        return title

recent_movies = []

for movie in favorite_movies:
    result = check_movie(movie)
    
    if result is not None:
        recent_movies.append(result)

print("Movies released after 2000:", recent_movies)
