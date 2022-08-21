import ipywidgets as widg
from IPython.display import display
import streamlit as st
import pandas as pd
import numpy as np

movies=pd.read_csv("movies.csv")
ratings=pd.read_csv("ratings.csv")
#title= st.text_input('Movie title', 'Life of Brian')
#st.write('The current movie title is', title)
ge=st.text_input("Genre(g):","Comedy")
th=st.text_input("Minimum reviews threshold(t):",0)
re=st.text_input("Num recommendations (N) :",0)

merged_left = pd.merge(left=movies, right=ratings, how='left', left_on='movieId', right_on='movieId')
out=merged_left[merged_left["genres"]==ge ].sort_values(by=["genres","rating","userId"], ascending=False)
out["Reviews"]=out.userId
out=out.reset_index(drop=True)
final=out[["title","rating","Reviews"]]
st.write(final.head(int(re)))

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)
