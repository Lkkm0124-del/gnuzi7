import streamlit as st
import pandas as pd
from textblob import TextBlob
from utils import youtube

st.title("💬 댓글 분석")

video_id = st.text_input("영상 ID")

if st.button("분석"):

    yt = youtube()

    comments = yt.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100
    ).execute()

    rows = []

    positive = 0
    negative = 0

    for item in comments["items"]:

        text = item["snippet"][
            "topLevelComment"
        ]["snippet"]["textDisplay"]

        score = TextBlob(text).sentiment.polarity

        if score > 0:
            positive += 1
        else:
            negative += 1

        rows.append(text)

    st.write(f"긍정 댓글 : {positive}")
    st.write(f"부정 댓글 : {negative}")

    df = pd.DataFrame({
        "댓글": rows
    })

    st.dataframe(df)
