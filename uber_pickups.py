import ipywidgets as widg
from IPython.display import display
import streamlit as st
import pandas as pd
import numpy as np

movies=pd.read_csv("movies.csv")
ratings=pd.read_csv("ratings.csv")
gen=widg.Text(description="Genre(g):")
thres=widg.IntText(description="Minimum reviews threshold(t):")
rec=widg.IntText(description="Num recommendations (N) :")
button = widg.Button(description="Check")
#button.on_click(on_button_clicked)
inputs=widg.VBox([gen,thres,rec])
interface=widg.VBox([inputs,button])
st.interface





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
