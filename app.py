import streamlit as st
import requests
from datetime import datetime
import pytz


def get_posts(id):
    url = f"https://pf-wapi.kakao.com/web/profiles/{id}/posts"
    req = requests.get(url)
    json = req.json()
    return json


def get_media(id, post_id):
    url = f"https://pf-wapi.kakao.com/web/profiles/{id}/posts/{post_id}"
    req = requests.get(url)
    json = req.json()
    return json.get("media", [])  # Return media or an empty list if not available


def show_store(store_id):
    try:
        posts = get_posts(store_id)
        post_ids = [p['id'] for p in posts.get('items', [])]
        images = []
        for post_id in post_ids:
            media = get_media(store_id, post_id)
            images.extend([m.get('xlarge_url', '') for m in media])
        if images:
            cols = st.columns(min(3, len(images)))
            for i, col in enumerate(cols):
                if i < len(images):
                    col.image(images[i], use_column_width=True)
        else:
            st.write("이 매장의 최근 게시물에는 이미지가 없어요")
    except Exception as e:
        st.error(f"에러가 발생했어요: {e}") 

# Page configuration
st.set_page_config(page_title="트렌드 트래커", page_icon="👕")

# Page title
st.title("신상 확인하실래요?")
st.write("---")

# Display current date
now = datetime.now(pytz.timezone("Asia/Seoul"))
st.metric(label="Current Date", value=now.strftime("%Y-%m-%d"))

# Display stores' posts and images
stores = {
    "Prada": "_Islxaj",
    "Balenciaga": "_wxofhxj",
    "YSL": "_rAMaxb",
    "Dior": "_dyBaT",
    "Givenchy": "_xicwixj",
    "Gucci": "_SQxceC",
    "Nike": "_fQxhxdz"
}

for store_name, store_id in stores.items():
    st.write(f"---\n## {store_name}")
    show_store(store_id)
