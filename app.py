# import streamlit as st
# import requests
# from datetime import datetime
# import pytz
# import pandas as pd
# from streamlit.components.v1 import html

# def get_posts(id):
#     url = f"https://pf-wapi.kakao.com/web/profiles/{id}/posts"
#     req = requests.get(url)
#     json = req.json()
#     return json

# def get_media(id, post_id):
#     url = f"https://pf-wapi.kakao.com/web/profiles/{id}/posts/{post_id}"
#     req = requests.get(url)
#     json = req.json()
#     media = json["media"]
#     return media

# def show_store(store_id):
#     posts = get_posts(store_id)
#     post_ids = [p['id'] for p in posts['items']]
#     images = []
#     for post_id in post_ids:
#         media = get_media(store_id, post_id)
#         for m in media:
#             images.append(m['xlarge_url'])
#     cols = st.columns(min(2, len(images)))
#     for i, col in enumerate(cols[:2]):
#         col.image(images[i])


# st.set_page_config(
#     page_title="신상 확인허실?",
#     page_icon="👕",
#     # layout="wide",
# )
# st.title("신상 조아함?")
# now = datetime.now(pytz.timezone("Asia/Seoul"))
# st.write("---")
# st.metric(
#     label="현재일자",
#     value=now.strftime("%Y-%m-%d"))
# st.write("---")

# show_store("_rAMaxb")

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
    media = json.get("media", []) # media 값이 없을 경우 빈 리스트 반환
    return media

def show_store(store_id):
    posts = get_posts(store_id)
    post_ids = [p['id'] for p in posts.get('items', [])] # items 값이 없을 경우 빈 리스트 반환
    images = []
    for post_id in post_ids:
        media = get_media(store_id, post_id)
        for m in media:
            images.append(m.get('xlarge_url', '')) # xlarge_url 값이 없을 경우 빈 문자열 반환
    if images:
        cols = st.columns(min(2, len(images)))
        for i, col in enumerate(cols):
            if i < len(images):
                col.image(images[i], use_column_width=True)
    else:
        st.write("이 매장의 최근 게시물에는 이미지가 없습니다.")

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

st.write('''
    ## 프라다 
''')
show_store("_Islxaj")

show_store("_wxofhxj")
