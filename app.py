import streamlit as st
from groq import Groq

# 1. Cấu hình trang Web
st.set_page_config(page_title="AI Translator - Demo", page_icon="🤖")

st.title("🤖 AI Translator Siêu Tốc")
st.write("Chạy trên Groq Llama 3 - Xây dựng bởi [Tên Bạn]")

# 2. Sidebar để nhập API Key (Để bảo mật, không hardcode key vào code)
with st.sidebar:
    st.header("Cấu hình")
    api_key = st.text_input("Nhập Groq API Key của bạn:", type="password")
    st.info("Lấy key miễn phí tại: https://console.groq.com/keys")

# 3. Giao diện chính
col1, col2 = st.columns(2)

with col1:
    st.header("Đầu vào")
    source_text = st.text_area("Nhập văn bản cần dịch:", height=200)
    target_lang = st.selectbox("Dịch sang ngôn ngữ:", ["Tiếng Anh", "Tiếng Việt", "Tiếng Nhật", "Tiếng Trung"])

with col2:
    st.header("Kết quả")
    
    # Nút bấm xử lý
    if st.button("Dịch ngay 🚀"):
        if not api_key:
            st.error("Vui lòng nhập API Key bên cột trái trước!")
        elif not source_text:
            st.warning("Vui lòng nhập văn bản cần dịch.")
        else:
            try:
                # Gọi API
                client = Groq(api_key=api_key)
                
                with st.spinner("Đang suy nghĩ..."):
                    chat_completion = client.chat.completions.create(
                        model="llama-3.1-8b-instant",
                        messages=[
                            {
                                "role": "system", 
                                "content": f"Bạn là chuyên gia dịch thuật. Hãy dịch văn bản sau sang {target_lang}. Chỉ trả về kết quả dịch, không giải thích gì thêm."
                            },
                            {
                                "role": "user", 
                                "content": source_text
                            }
                        ],
                        temperature=0.3, # Dịch thuật cần chính xác
                    )
                    
                    # Hiển thị kết quả
                    result = chat_completion.choices[0].message.content
                    st.success("Hoàn thành!")
                    st.text_area("Bản dịch:", value=result, height=200)
                    
            except Exception as e:
                st.error(f"Có lỗi xảy ra: {str(e)}")