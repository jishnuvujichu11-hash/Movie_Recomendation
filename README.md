# 🎬 Movie Recommendation System

A **Content-Based Movie Recommendation System** built with **Python**, **Streamlit**, **Scikit-learn**, and **TMDB**. This application recommends movies similar to a selected movie by analyzing genres, keywords, cast, crew, and other metadata using **TF-IDF Vectorization** and **Cosine Similarity**.

---

## 📌 Features

- 🎥 Search and select a movie from the dataset.
- 🤖 Content-based recommendation engine.
- 📊 Recommends the top 5 similar movies.
- 🖼️ Displays movie posters.
- ⚡ Fast recommendations using precomputed similarity matrix.
- 🌐 Interactive web interface built with Streamlit.

---

## 🛠️ Technologies Used

- Python 3.x
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Requests
- Pickle
- TMDB API

---

## 📂 Project Structure

```text
Movie Recommendation/
│
├── app.py                     # Streamlit application
├── movies.pkl                 # Processed movie dataset & cosine similarity
├── movie_posters.csv          # Movie poster URLs
├── download_posters.py        # Script to download poster URLs
├── requirements.txt           # Project dependencies
├── tmdb_5000_movies.csv       # Original movie dataset
├── tmdb_5000_credits.csv      # Original credits dataset
└── README.md
```

---

## 📊 Dataset

This project uses the **TMDB 5000 Movie Dataset**, which contains movie metadata such as:

- Movie Title
- Genres
- Keywords
- Cast
- Crew
- Overview
- Movie ID

These features are combined into a single text field and transformed into numerical vectors using **TF-IDF**.

---

## ⚙️ How It Works

1. Load the movie and credits datasets.
2. Merge both datasets using the movie title.
3. Clean and preprocess the data.
4. Extract:
   - Genres
   - Keywords
   - Top Cast
   - Director
   - Overview
5. Combine these features into a single **tags** column.
6. Convert the text into TF-IDF vectors.
7. Compute cosine similarity between all movies.
8. Save the processed data using **Pickle**.
9. Build an interactive Streamlit application to display recommendations.

---

## 🧠 Recommendation Algorithm

The recommendation engine uses:

- **TF-IDF Vectorizer** to convert textual movie metadata into numerical feature vectors.
- **Cosine Similarity** to measure similarity between movies.

Movies with the highest cosine similarity scores are recommended.

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
```

```bash
cd movie-recommendation-system
```

### Create a virtual environment

```bash
python -m venv movie-env
```

### Activate the virtual environment

**Windows**

```bash
movie-env\Scripts\activate
```

**macOS/Linux**

```bash
source movie-env/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will start locally, typically at:

```text
http://localhost:8501
```

---

## 📷 Download Movie Posters

To download and store poster URLs locally:

```bash
python download_posters.py
```

This generates:

```text
movie_posters.csv
```

which is used by the Streamlit application to display movie posters efficiently.

---

## 📸 Application Preview

The application provides:

- Movie selection dropdown
- Recommendation button
- Five recommended movies
- Movie posters
- Responsive Streamlit interface

---

## 📈 Future Improvements

- Movie search with autocomplete
- Genre-based filtering
- IMDb/TMDB ratings
- Movie overview and release year
- Movie trailers
- User authentication
- Favorite movies
- Hybrid recommendation system
- Collaborative filtering
- Deployment on Streamlit Community Cloud

---

## 👨‍💻 Author

**Jishnu Vu**

Aspiring Data Analyst | Python | SQL | Power BI | Machine Learning
