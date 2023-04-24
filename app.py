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

def load_image_from_url(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

# 카카오톡 채널 게시글에서 이미지를 가져와서 화면에 표시하는 Streamlit 앱
def main():
    st.title("카카오톡 채널 게시글 이미지 불러오기")
    id = st.text_input("채널 ID를 입력하세요.")
    
    if id:
        try:
            posts = get_posts(id)
            for post in posts:
                st.write(f"게시글 ID: {post['id']}")
                media = get_media(id, post['id'])
                for item in media:
                    if item["type"] == "PHOTO":
                        url = item["url"]
                        img = load_image_from_url(url)
                        st.image(img, caption="불러온 이미지")
        except:
            st.error("올바른 채널 ID를 입력해주세요.")
    
if __name__ == "__main__":
    main()



# def show_store(store_id):
#     posts = get_posts(store_id)
#     post_ids = [p['id'] for p in posts['items']]
#     images = []
#     for post_id in post_ids:
#         media = get_media(store_id, post_id)
#         for m in media:
#             if 'xlarge_url' in m:  # 'xlarge_url' 키가 있는 경우에만 추가
#                 images.append(m['xlarge_url'])
#     cols = st.columns(min(3, len(images)))
#     for i, col in enumerate(cols[:3]):
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
# st.write("### ㅎㅇ")

# show_store("_fQxhxdz")

