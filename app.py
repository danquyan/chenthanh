import streamlit as st
import pandas as pd

# 🔧 Cấu hình tiêu đề và bố cục
st.set_page_config(page_title="Chén Thánh Options Flow", layout="wide")
st.title("📈 Phân Tích Dòng Tiền Options (Chén Thánh V4)")

# 📁 Bước 1: Tải file CSV lên
uploaded_file = st.file_uploader("📂 Tải lên file .csv dữ liệu dòng tiền từ Unusual Whales", type=["csv"])

# 📊 Bước 2: Kiểm tra nếu đã có file
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # ✅ Hiển thị cột có trong file CSV
    st.write("🧾 Các cột có trong file CSV:", df.columns.tolist())

    try:
        # ⚠️ THAY ĐÚNG TÊN CỘT TƯƠNG ỨNG TRONG FILE CỦA BẠN
        df["score"] = df["size"] * df["premium"] / (df["spread"] + 0.0001)
        df["score"] = df["score"].rank(pct=True) * 10  # chuẩn hóa điểm từ 0 đến 10

        # 📊 Hiển thị bảng kết quả
        st.subheader("🔥 Top tín hiệu dòng tiền nổi bật")
        st.dataframe(df.sort_values("score", ascending=False).head(20), use_container_width=True)

    except KeyError as e:
        st.error(f"❌ Lỗi: Cột '{e}' không tồn tại trong file CSV. Vui lòng kiểm tra lại tên cột.")

else:
    st.warning("⚠️ Vui lòng tải lên file CSV để bắt đầu phân tích.")
