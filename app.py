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


def show_store(store_id):
    posts = get_posts(store_id)
    images = []
    for post in posts["items"]:
        if "media" in post and post["media"] is not None:
            media = post["media"]
            for m in media:
                if m is not None and "xlarge_url" in m:
                    images.append(m["xlarge_url"])
    cols = st.columns(min(3, len(images)))
    for i, col in enumerate(cols[:3]):
        col.image(images[i])



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

show_store("_qRuGz")

