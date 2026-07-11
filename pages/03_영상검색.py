import streamlit as st
from utils import youtube

st.title("🎥 영상 검색")

keyword = st.text_input("검색어")

if st.button("검색"):

    yt = youtube()

    result = yt.search().list(
        q=keyword,
        part="snippet",
        type="video",
        maxResults=20
    ).execute()

    for item in result["items"]:

        video_id = item["id"]["videoId"]

        title = item["snippet"]["title"]

        st.subheader(title)

        st.video(
            f"https://www.youtube.com/watch?v={video_id}"
        )

        st.divider()
