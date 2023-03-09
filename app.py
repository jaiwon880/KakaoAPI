import streamlit as st
import requests

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

def show_menus(store_id):
    posts = get_posts(store_id)
    post_ids = [p['id'] for p in posts['items']]
    images = []
    for post_id in post_ids:
        media = get_media(store_id, post_id)
        for m in media:
            images.append(m['xlarge_url'])
    cols = st.columns(len(images))
    for i, col in enumerate(cols)[:3]:
        col.image(images[i])

st.write("# 6300원의 행복")
st.write("## The 좋은밥상")
show_menus("_xfWxfCxj")
st.write("## 우림구내식당")
show_menus("_ixcNxexj")
