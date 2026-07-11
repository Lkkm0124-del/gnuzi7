import streamlit as st
from utils import youtube

st.title("🔍 유튜버 검색")

channel_name = st.text_input("유튜버 이름")

if st.button("검색"):

    yt = youtube()

    result = yt.search().list(
        q=channel_name,
        part="snippet",
        type="channel",
        maxResults=10
    ).execute()

    for item in result["items"]:

        channel_id = item["snippet"]["channelId"]

        info = yt.channels().list(
            part="statistics,snippet",
            id=channel_id
        ).execute()

        data = info["items"][0]

        st.subheader(data["snippet"]["title"])

        st.write(
            f"구독자 : {data['statistics'].get('subscriberCount','비공개')}"
        )

        st.write(
            f"총 조회수 : {data['statistics'].get('viewCount','0')}"
        )

        st.write(
            f"영상 수 : {data['statistics'].get('videoCount','0')}"
        )

        st.divider()
