import streamlit as st
import requests
from datetime import datetime
import pytz
from concurrent.futures import ThreadPoolExecutor

# Streamlit 캐시 사용
# @st.cache 데코레이터를 사용하여 API 호출을 캐시 
# 같은 요청에 대해 데이터가 이미 캐시에 있다면 다시 API를 호출하지 않고 캐시된 데이터를 사용

# Page configuration
st.set_page_config(page_title="트렌드 트래커", page_icon="👕")

# Page title
st.title("신상 확인하실래요?")
st.write("---")

# Display current date
now = datetime.now(pytz.timezone("Asia/Seoul"))
st.metric(label="Current Date", value=now.strftime("%Y-%m-%d"))


@st.cache
def get_posts(id):
    url = f"https://pf-wapi.kakao.com/web/profiles/{id}/posts"
    req = requests.get(url)
    json = req.json()
    return json

@st.cache
def get_media(id, post_id):
    url = f"https://pf-wapi.kakao.com/web/profiles/{id}/posts/{post_id}"
    req = requests.get(url)
    json = req.json()
    return json.get("media", [])  # Return media or an empty list if not available


def fetch_store_images(store_id):
    images = []
    try:
        posts = get_posts(store_id)
        post_ids = [p['id'] for p in posts.get('items', [])]
        for post_id in post_ids:
            media = get_media(store_id, post_id)
            images.extend([m.get('xlarge_url', '') for m in media])
    except Exception as e:
        pass
    return images

stores = {
    "Prada": "_Islxaj",
    "Balenciaga": "_wxofhxj",
    "YSL": "_rAMaxb",
    "Dior": "_dyBaT",
    "Givenchy": "_xicwixj",
    "Gucci": "_SQxceC",
    "Nike": "_fQxhxdz"
}

# 병렬 처리 적용
with ThreadPoolExecutor() as executor:
    store_images = list(executor.map(fetch_store_images, stores.values()))


# 이미지 표시
for store_name, images in zip(stores.keys(), store_images):
    st.write(f"---\n## {store_name}")
    if images:
        cols = st.columns(min(3, len(images)))
        for i, col in enumerate(cols):
            if i < len(images):
                col.image(images[i], use_column_width=True)
    else:
        st.write("이 매장의 최근 게시물에는 이미지가 없어요")
