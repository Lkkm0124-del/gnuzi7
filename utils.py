import streamlit as st
from googleapiclient.discovery import build

def youtube():
    api_key = st.secrets["YOUTUBE_API_KEY"]

    return build(
        "youtube",
        "v3",
        developerKey=api_key
    )
