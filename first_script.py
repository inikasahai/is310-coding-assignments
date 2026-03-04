favorite_movies = [
    {"title": "Lights Out", "year": 2016},
    {"title": "Scream", "year": 1996},
    {"title": "Superman", "year": 1978},
    {"title": "Inside Out", "year": 2015},
    {"title": "Zootopia 2", "year": 2025}
]

def check_movie(movie):
    if movie["year"] < 2000:
        print("This movie was released before 2000")
        return None
    else:
        print("This movie was released after 2000")
        return movie["title"]

recent_movies = []

for movie in favorite_movies:
    result = check_movie(movie)
    
    if result is not None:
        recent_movies.append(result)

print(recent_movies)