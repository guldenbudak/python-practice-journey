movies = [
    {"title": "Film A", "rating": 7.2},
    {"title": "Film B", "rating": 8.9},
    {"title": "Film C", "rating": 8.1},
    {"title": "Film D", "rating": 9.0},
    {"title": "Film E", "rating": 6.5},
    {"title": "Film F", "rating": 7.8},
    {"title": "Film G", "rating": 8.3},
    {"title": "Film H", "rating": 7.0},
    {"title": "Film I", "rating": 8.6},
    {"title": "Film J", "rating": 6.9},
    {"title": "Film K", "rating": 9.1},
    {"title": "Film L", "rating": 7.4},
    {"title": "Film M", "rating": 8.0},
    {"title": "Film N", "rating": 7.7},
    {"title": "Film O", "rating": 8.5}
]
new_list = sorted(movies, key=lambda x: x["rating"], reverse=True)
print(new_list)
print("First three films\n", (movies[0]["title"]))
print((movies[1]["title"]))
print((movies[2]["title"]))