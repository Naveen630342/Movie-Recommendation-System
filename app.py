import streamlit as st
import nltk 
import sklearn
import pandas as pd
import pickle 
import joblib


st.title("Movie Recommendation System")

with open("movies.pickle",'rb') as m:
    movies = pickle.load(m)

similarites = joblib.load('similarites.joblib')

movie_names=movies['title'].values
def recommend(name_movie):
    movie_index=movies[movies['title']==name_movie].index[0]
    recommendations=similarites[movie_index]
    movie_list = sorted(enumerate(recommendations), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

name_movie=st.selectbox("Enter the Movie Name",movie_names)

if st.button("Recommend"):
    r=recommend(name_movie)
    st.write("Recommended Movies are:")
    for movie in r:
        st.write(movie)