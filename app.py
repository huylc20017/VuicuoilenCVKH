
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Báo Cáo CVKHCN", layout="wide")

st.title("📊 Báo Cáo Bán Hàng Theo CVKHCN")

# Load data
df = pd.read_csv("cleaned_bao_cao.csv")

# Hiển thị bảng dữ liệu
st.subheader("📋 Bảng dữ liệu gốc")
st.dataframe(df)

# Biểu đồ TOI theo nhân sự
st.subheader("📈 Biểu đồ TOI theo nhân sự")
toi_data = [26.022149000000017, 130.21928400000007, 204.1724870000001, 82.14610400000005, 161.53670300000007, 0]
nhan_su = ['HOANGVANTHANH', 'NGUYENDINHLUAN', 'NGUYENTHANHHA', 'TADUCTHANH', 'TANGXUANHOC', 'LETHIBON']
fig, ax = plt.subplots()
ax.bar(nhan_su, toi_data, color="skyblue")
ax.set_ylabel("TOI (triệu đồng)")
ax.set_xlabel("Nhân sự")
ax.set_title("TOI theo nhân sự")
st.pyplot(fig)

# Biểu đồ số lượng KH vay mới
st.subheader("👥 Số lượng KH vay mới theo nhân sự")
kh_vay_moi = [2, 1, 1, 5, 1, 0]
fig2, ax2 = plt.subplots()
ax2.bar(nhan_su, kh_vay_moi, color="orange")
ax2.set_ylabel("Số lượng KH")
ax2.set_xlabel("Nhân sự")
ax2.set_title("Số lượng KH vay mới")
st.pyplot(fig2)
