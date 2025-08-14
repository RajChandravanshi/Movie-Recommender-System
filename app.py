import pickle
import streamlit as st

def recommend(movie):
    """Recommend top 5 similar movies title."""
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True)
    
    recommended_movie_names = []
    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]]['title'])
    
    return recommended_movie_names


# ---------------- STREAMLIT UI ----------------
st.header("Movie Recommender System")

# Load data
movies = pickle.load(open("movie_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

# Dropdown for movie selection
movie_list = movies["title"].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# Button to show recommendations
if st.button("Show Recommendation"):
    names = recommend(selected_movie)
    for name in names:
        st.write(name)
