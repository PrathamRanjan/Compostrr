import streamlit as st
from streamlit_player import st_player
import pandas as pd

# Correctly setting the page config as the first command
st.set_page_config(page_title="Composter", layout="wide")

# Function to load and apply CSS for styling (ensure this doesn't contain Streamlit commands that render content)
def load_css():
    css = """
    <style>
        body {
            background-color: #000000; /* Black background */
            color: #FFFFFF; /* White text */
        }
        .stApp {
            background-color: #000000;
            color: #FFFFFF;
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

load_css()  # Apply the CSS for styling

# Following Streamlit commands to set up your app
st.title("Compostrr")
st.write("Good Morning Amanda, your Compostrr is at 51% complete.")

# Section 1: Composting Courses and Content
st.header("Composting Courses and Content")

# Embedding YouTube video
video_url = "https://www.youtube.com/watch?v=nxTzuasQLFo"
st_player(video_url)

st.write("You have completed 41% of our composting course, complete all to become a registered CompostrR.")

# Section 2: Find nearby Compostrr’s
st.header("Find Nearby Compostrr’s")

# Coordinates for Ang Mo Kio, Singapore
ang_mo_kio_coords = {'latitude': [1.3691], 'longitude': [103.8454]}

# Create a DataFrame with these coordinates
df_coords = pd.DataFrame(data=ang_mo_kio_coords)

# Use the DataFrame to display the map
st.map(data=df_coords, zoom=11)
