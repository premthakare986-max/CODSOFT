import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = {
    "title": ["Avatar", "Titanic", "Avengers", "Iron Man", "Inception"],
    "genre": ["Action Adventure", "Romance Drama", "Action Superhero", "Action Superhero", "Sci-Fi Thriller"]
}

movies = pd.DataFrame(data)

vectorizer = CountVectorizer()
matrix = vectorizer.fit_transform(movies["genre"])

similarity = cosine_similarity(matrix)

def recommend(movie):
    index = movies[movies["title"] == movie].index[0]
    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print("Recommended Movies:")
    for i in scores[1:]:
        print(movies.iloc[i[0]]["title"])

movie = input("Enter movie name: ")
recommend(movie)