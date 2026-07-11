import streamlit as st
import pandas as pd
import plotly.express as px
from utils import youtube

st.title("📈 조회수 통계")

channel_id = st.text_input("채널 ID")

if st.button("분석"):

    yt = youtube()

    videos = yt.search().list(
        part="snippet",
        channelId=channel_id,
        maxResults=50,
        order="date",
        type="video"
    ).execute()

    rows = []

    for item in videos["items"]:

        video_id = item["id"]["videoId"]

        stats = yt.videos().list(
            part="statistics,snippet",
            id=video_id
        ).execute()

        if len(stats["items"]) == 0:
            continue

        data = stats["items"][0]

        rows.append({
            "제목": data["snippet"]["title"],
            "조회수": int(
                data["statistics"].get("viewCount",0)
            )
        })

    if rows:

        df = pd.DataFrame(rows)

        fig = px.bar(
            df,
            x="제목",
            y="조회수",
            title="영상별 조회수"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.dataframe(df)
