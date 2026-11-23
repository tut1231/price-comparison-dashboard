import streamlit as st
import pandas as pd
from pathlib import Path

# 設定網頁標題
st.set_page_config(page_title="price-comparison-dashboard", page_icon="🛒",layout="wide")
st.title("🛒跨電商平台商品比價、折扣深度分析與促銷價差儀表板")
st.caption("支援通路：PChome 24h 購物、博客來、Yahoo 奇摩購物中心、momo 購物網")
keyword = st.text_input(
    label="商品名稱 / 型號關鍵字",
    placeholder="請輸入商品名稱、型號 ",
)

#@st.cache_data(ttl='1h') #從 HTTP 端點（網址/API）讀取資料，快取有效期限為 1 小時
#def get_B2C_data( ):

# ------------------------------------------------------------