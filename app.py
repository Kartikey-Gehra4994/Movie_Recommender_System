from flask import Flask, render_template, request
import requests
import pickle
import os
from dotenv import load_dotenv

# Load environment variables (API key)
load_dotenv()

app = Flask(__name__)

# create Movies.pkl, similarity.pkl file if not exist
def download_file(url, filename):
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        r = requests.get(url)
        with open(filename, "wb") as f:
            f.write(r.content)
        print(f"{filename} Downloaded!")
    
# GitHub Release link
movies_url = "https://github.com/Kartikey-Gehra4994/Movie_Recommender_System/releases/download/v1.0/movies.pkl"
similarity_url = "https://github.com/Kartikey-Gehra4994/Movie_Recommender_System/releases/download/v1.0/similarity.pkl"

# Download if not present
download_file(movies_url, "movies.pkl")
download_file(similarity_url, "similarity.pkl")

# Load preprocessed data and similarity matrix
new_df = pickle.load(open("movies.pkl", "rb"))
similatity = pickle.load(open("similarity.pkl", "rb"))

# TMDB API key
movies_api_key = os.getenv("TMDB_API_KEY")

# Fetch movie poster from TMDB API
def featch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={movies_api_key}&language=en-US"
        response = requests.get(url)

        # Check API response
        if response.status_code != 200:
                return "https://via.placeholder.com/300x450?text=No+Image"

        data = response.json()
        poster_path = data.get("poster_path")

        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://image.tmdb.org/t/p/w500?text=No+Image"
    except Exception:
        return "https://via.placeholder.com/300x450?text=Error"
 

# Recommend top 5 similar movies
def recommend(movie):
    # If movie not found in dataset
    if movie not in new_df['title'].values:
        return [], []

    # Get index of selected movie
    movie_index = new_df[new_df["title"] == movie].index[0]

    # Get similarity scores
    distances = similatity[movie_index]

    # Sort and pick top 5 similar movies
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []

    # Fetch movie names and posters
    for i in movies_list:
        movie_id = new_df.iloc[i[0]].movie_id
        recommended_movies.append(new_df.iloc[i[0]].title)
        recommended_movies_poster.append(featch_poster(movie_id))

    return recommended_movies, recommended_movies_poster


# Main route (home page)
@app.route("/", methods=["GET", "POST"])
def hello_world():
    movie = request.form.get("movie")

    # handel empty input
    if not movie or movie.strip() == "":
        movie_name,movie_poster = [],[]
    else:
        movie_name,movie_poster = recommend(movie)

    return render_template(
        "index.html",
        movie_list=new_df["title"].values,
        movie_name=movie_name,
        movie_poster=movie_poster
    )

if __name__ == '__main__':
    app.run()