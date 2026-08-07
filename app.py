import streamlit as st
import pickle
import pandas as pd
import requests

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1 {
    text-align: center;
}

.stButton > button {
    width: 100%;
    border-radius: 10px;
    font-weight: bold;
    background-color: #FF4B4B;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ---------------- #
poster_df = pd.read_csv("movie_posters.csv")


@st.cache_data
def load_data():
    with open("movies.pkl", "rb") as file:
        movies, cosine_sim = pickle.load(file)
    return movies, cosine_sim


movies, cosine_sim = load_data()

movies = movies.merge(
    poster_df,
    on=["movie_id", "title"],
    how="left"
)

# ---------------- TMDB API ---------------- #




def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"

    response = requests.get(url)

    data = response.json()

    poster_path = data.get("poster_path")

    if poster_path:
        return "https://image.tmdb.org/t/p/w500" + poster_path

    return "https://via.placeholder.com/500x750?text=No+Poster"

# ---------------- RECOMMENDATION ---------------- #

def get_recommendations(movie):

    movie_index = movies[movies["title"] == movie].index[0]

    distances = cosine_sim[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    movie_names = []
    movie_posters = []

    for i in movie_list:

        movie_names.append(
            movies.iloc[i[0]].title
        )

        movie_posters.append(
            movies.iloc[i[0]].poster
        )

    return movie_names, movie_posters

# ---------------- SIDEBAR ---------------- #

st.sidebar.header("🎥 Movie Finder")

selected_movie = st.sidebar.selectbox(
    "Select a Movie",
    movies["title"].values
)

recommend_button = st.sidebar.button(
    "🎬 Get Recommendations",
    use_container_width=True
)

# ---------------- HEADER ---------------- #

st.title("🎬 Movie Recommendation System")

st.write(
    "Discover movies similar to your favourite movie using "
    "**Content-Based Recommendation** with **TF-IDF** and **Cosine Similarity**."
)

st.divider()

# ---------------- METRICS ---------------- #

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Movies", len(movies))

with col2:
    st.metric("Recommendations", 5)

with col3:
    st.metric("Algorithm", "TF-IDF")

st.divider()

# ---------------- RECOMMENDATIONS ---------------- #

if recommend_button:

    with st.spinner("Finding similar movies..."):

        movie_names, posters = get_recommendations(selected_movie)

    st.success("Top 5 Recommendations")

    cols = st.columns(5)

    for col, name, poster in zip(cols, movie_names, posters):

        with col:

            if pd.notna(poster):

                st.image(
                    poster,
                    use_container_width=True
                )

            else:

                st.image(
                    "https://via.placeholder.com/500x750?text=No+Poster",
                    use_container_width=True
                )

            st.markdown(
                f"<h5 style='text-align:center'>{name}</h5>",
                unsafe_allow_html=True
            )