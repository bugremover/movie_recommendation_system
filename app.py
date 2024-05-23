import pickle
import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Movie Recommendation System", page_icon="🎬", layout="wide")

# Title and description
st.title('🎥 Movie Recommendation System')
st.markdown("""
Welcome to the Movie Recommendation System! This app uses machine learning to suggest movies based on your preferences.
""")

# Load the pickled files
try:
    with open('artificats/movie_list.pkl', 'rb') as file:
        movies = pickle.load(file)
    # Ensure the 'movies' DataFrame is correctly loaded
    if isinstance(movies, pd.DataFrame):
        st.success("Movies DataFrame loaded successfully.")
    else:
        st.error("Failed to load the Movies DataFrame correctly.")
        st.stop()

    # Display the first few rows of the DataFrame to verify its structure
    st.subheader('Movies Data Preview')
    st.dataframe(movies.head())
    
    movie_list = movies['title'].values
    selected_movie = st.selectbox(
        "Type or select a movie from the dropdown",
        movie_list
    )

    # You can add more functionality here, such as recommending movies based on the selection
    st.write(f"Selected Movie: {selected_movie}")

except Exception as e:
    st.error(f"An error occurred: {e}")
    st.stop()
