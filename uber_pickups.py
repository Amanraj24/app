import ipywidgets as widg
from IPython.display import display
import streamlit as st
import pandas as pd
import numpy as np

movies=pd.read_csv("movies.csv")
ratings=pd.read_csv("ratings.csv")
