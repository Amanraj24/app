import ipywidgets as widg
from IPython.display import display
import streamlit as st
import pandas as pd
import numpy as np

option = st.selectbox(
     'Select Type of Recommender System',
     ('Popularity-Based Recommender System', 'Content-Based Recommender System', 'Collaborative Based Recommender System'))


st.title(option)
movies=pd.read_csv("movies.csv")
ratings=pd.read_csv("ratings.csv")
type_movies=movies.groupby("genres")["movieId"].sum().sort_values(ascending=False)
st.write("List of Genres")
st.write(type_movies.drop(columns="movieId"))
#title= st.text_input('Movie title', 'Life of Brian')
#st.write('The current movie title is', title)


merged_left = pd.merge(left=movies, right=ratings, how='left', left_on='movieId', right_on='movieId')
if option=='Popularity-Based Recommender System':
     ge=st.text_input("Genre(g):","Comedy")
     th=st.text_input("Minimum reviews threshold(t):",0)
     re=st.text_input("Num recommendations (N) :",0)
     out=merged_left[merged_left["genres"]==ge ].sort_values(by=["genres","rating","userId"], ascending=False)
     out=out[out["userId"]>=int(th)]
     out["Num Reviews"]=out.userId.astype("int")
     out["Movie Title"]=out.title
     out["Average Movie Rating"]=out.rating.astype("float")
     out=out.reset_index(drop=True)
     final=out[["Movie Title","Average Movie Rating","Num Reviews"]]
     st.write(final.head(int(re)))
elif option=='Content-Based Recommender System':
     for i in range(0,len(movies)):
          Str = movies["title"][i]
          l = len(Str)
          Remove_last = Str[:l-7]
          movies["title"][i]=Remove_last
     n_movies=movies
     mv=st.text_input("Movie Title (t): ")
     rec=st.text_input("Num recommendations (N):")
     movie=n_movies[n_movies["title"]==mv]
     
     id1=movie["movieId"].tolist()
     id2=st.text(id1[0])
     genre=merged_left[merged_left["movieId"]==eval(id2)]["genres"]
     genre=genre.unique()
     ge=st.text(genre.tolist()[0])
     out2=merged_left[merged_left["genres"]==ge ].sort_values(by=["genres","rating","userId"], ascending=False)
     out2=out2.title.head(int(rec))
     st.write(out2)


#DATE_COLUMN = 'date/time'
#DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
#            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

#@st.cache
#def load_data(nrows):
#   data = pd.read_csv(DATA_URL, nrows=nrows)
#    lowercase = lambda x: str(x).lower()
#    data.rename(lowercase, axis='columns', inplace=True)
#    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#    return data
#
#data_load_state = st.text('Loading data...')
#data = load_data(10000)
#data_load_state.text("Done! (using st.cache)")

#if st.checkbox('Show raw data'):
#    st.subheader('Raw data')
#    st.write(data)

#st.subheader('Number of pickups by hour')
#hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
#st.bar_chart(hist_values)

# Some number in the range 0-23
#hour_to_filter = st.slider('hour', 0, 23, 17)
#filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

#st.subheader('Map of all pickups at %s:00' % hour_to_filter)
#st.map(filtered_data)
