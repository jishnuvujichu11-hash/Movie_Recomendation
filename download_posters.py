import pickle
import pandas as pd
import requests
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from dotenv import load_dotenv
import os
load_dotenv()


# ---------------- CONFIG ---------------- #

API_KEY = os.getenv("API_KEY_poster")

OUTPUT_FILE = "movie_posters.csv"

# ---------------- LOAD MOVIES ---------------- #

with open("movies.pkl", "rb") as file:
    movies, cosine_sim = pickle.load(file)

# ---------------- SESSION WITH RETRIES ---------------- #

session = requests.Session()

retry = Retry(
    total=5,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET"]
)

adapter = HTTPAdapter(max_retries=retry)

session.mount("https://", adapter)
session.mount("http://", adapter)

# ---------------- DOWNLOAD ---------------- #

poster_urls = []

total_movies = len(movies)

for index, row in movies.iterrows():

    movie_id = row["movie_id"]

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"

    poster = None

    try:

        response = session.get(url, timeout=10)

        response.raise_for_status()

        data = response.json()

        if data.get("poster_path"):

            poster = (
                "https://image.tmdb.org/t/p/w500"
                + data["poster_path"]
            )

        print(f"[{index+1}/{total_movies}] ✅ {row['title']}")

    except Exception as e:

        print(f"[{index+1}/{total_movies}] ❌ {row['title']}")
        print(e)

    poster_urls.append(poster)

    # Be polite to the API
    time.sleep(0.25)

    # Save every 100 movies
    if (index + 1) % 100 == 0:

        temp = movies.iloc[:len(poster_urls)].copy()

        temp["poster"] = poster_urls

        temp[["movie_id", "title", "poster"]].to_csv(
            OUTPUT_FILE,
            index=False
        )

        print(f"\n💾 Saved progress ({index+1} movies)\n")

# ---------------- FINAL SAVE ---------------- #

movies["poster"] = poster_urls

movies[["movie_id", "title", "poster"]].to_csv(
    OUTPUT_FILE,
    index=False
)

print("\n🎉 All posters downloaded successfully!")