import streamlit as st
import os,sys

sys.path.append(os.getcwd())

from module.hello import hello




# 设置标题
st.title("Streamlit 简单示例")

# 添加用户输入框
number = st.number_input("输入一个数值", min_value=0.0, max_value=100.0, value=1.0, step=0.1)

# 按钮触发事件
if st.button("计算平方"):
    result = number ** 2
    st.write(f"{number} 的平方是 {result}")
    st.write(hello())

# 添加文件上传功能
uploaded_file = st.file_uploader("上传一个文件")

# 展示上传文件的内容
if uploaded_file is not None:
    st.write(f"你上传了文件：{uploaded_file.name}")


# streamlit run demo.py