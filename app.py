import streamlit as st

import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie_name = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id =  movies.iloc[i[0]].movie_id
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movie_name.append(movies.iloc[i[0]].title)

    return recommended_movie_name, recommended_movies_poster




movies_list=pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_list)
similarity=pickle.load(open('similarity.pkl','rb'))

st.title('movie recommender system')

selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values)

if st.button('recommend movie'):
    recommended_movie_name,recommended_movies_poster = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_name[0])
        st.image(recommended_movies_poster[0])
    with col2:
        st.text(recommended_movie_name[1])
        st.image(recommended_movies_poster[1])

    with col3:
        st.text(recommended_movie_name[2])
        st.image(recommended_movies_poster[2])
    with col4:
        st.text(recommended_movie_name[3])
        st.image(recommended_movies_poster[3])
    with col5:
        st.text(recommended_movie_name[4])
        st.image(recommended_movies_poster[4])