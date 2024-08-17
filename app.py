import streamlit as st
st.title("Movie Recommandor System")

import pandas as pd

import pickle

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}/videos?api_key=b2d211f595d3a98bfaced58eec69b24b&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    st.text("https://api.themoviedb.org/3/movie/{}/videos?api_key=b2d211f595d3a98bfaced58eec69b24b&language=en-US".format(movie_id))
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True,key = lambda x: x[1])

    recom = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = i[0]

        # poster

        recom.append(movies.iloc[i[0]].title)
    return recom

movie_list = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_list)
similarity = pickle.load(open('similarity.pkl', 'rb'))
similarity = pd.DataFrame(similarity)


option = st.selectbox(
    "Movie Recommendation",
    movies['title'].values
)
if st.button('recommend'):
    recommendation = recommend(option)
    for i in recommendation:
        st.write(i)