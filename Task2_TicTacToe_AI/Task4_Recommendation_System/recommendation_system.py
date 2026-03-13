import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv("movies.csv")

# Convert genre text to numbers
vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(movies["genre"])

# Calculate similarity
similarity = cosine_similarity(genre_matrix)

# Function to recommend movies
def recommend(movie_title):
    movie_index = movies[movies["title"] == movie_title].index[0]
    scores = list(enumerate(similarity[movie_index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print("Recommended Movies:")

    for i in scores[1:6]:
        print(movies.iloc[i[0]]["title"])

# User input
movie = input("Enter a movie name: ")
recommend(movie)