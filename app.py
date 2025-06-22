
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Chén Thánh Options Flow", layout="wide")

st.title("📈 Phân Tích Dòng Tiền Options (Chén Thánh V4)")

uploaded_file = st.file_uploader("📤 Tải lên file .csv dữ liệu dòng tiền từ Unusual Whales", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Tính điểm tín hiệu nâng cao (ví dụ sơ bộ)
    df["score"] = df["size"] * df["premium"] / (df["spread"] + 0.0001)
    df["score"] = df["score"].rank(pct=True) * 10  # Chuẩn hóa điểm

    # Hiển thị bảng
    st.subheader("📊 Top tín hiệu dòng tiền nổi bật")
    st.dataframe(df.sort_values("score", ascending=False).head(20), use_container_width=True)
else:
    st.warning("⚠️ Vui lòng tải lên file CSV để bắt đầu phân tích.")
