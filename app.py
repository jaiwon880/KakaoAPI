import streamlit as st
import requests
from datetime import datetime
import pytz
import pandas as pd
from streamlit.components.v1 import html

def get_posts(id):
    url = f"https://pf-wapi.kakao.com/web/profiles/{id}/posts"
    req = requests.get(url)
    json = req.json()
    return json

def get_media(id, post_id):
    url = f"https://pf-wapi.kakao.com/web/profiles/{id}/posts/{post_id}"
    req = requests.get(url)
    json = req.json()
    media = json["media"]
    return media


def show_kakao_posts(channel_id):
    posts = get_posts(channel_id)
    for post in posts['items']:
        st.write('===')
        st.write('작성 시간:', post['createdAt'])
        st.write('내용:', post['content'])
        media = get_media(channel_id, post['id'])
        if media:
            st.write('이미지:')
            for m in media:
                if 'xlarge_url' in m:
                    st.image(m['xlarge_url'])


st.set_page_config(
    page_title="신상 확인허실?",
    page_icon="👕",
    # layout="wide",
)
st.title("신상 조아함?")
now = datetime.now(pytz.timezone("Asia/Seoul"))
st.write("---")
st.metric(
    label="현재일자",
    value=now.strftime("%Y-%m-%d"))
st.write("---")
st.write("### ㅎㅇ")

show_store("_fQxhxdz")