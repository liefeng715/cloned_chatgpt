import streamlit as st
from video_project import generator_script

st.title("视频脚本生成器")
with st.sidebar:
    openai_api_key = st.text_input("请输入你的API密钥",type="password")
    st.markdown("[获取OpenAI API密钥](https://platform.openai.com/account/api-keys)")

subject = st.text_input("请输入你的主题")
video_long = st.number_input("请选择你的视频时长（分钟）",min_value=0.1,step=0.1)
creativity = st.slider("请选择生成视频脚本的创造性（创造性越高，文本越具有多样性",min_value=0.1,
                       max_value=1.0,value=0.4,step=0.1)
submit = st.button("生成脚本")
if submit and not openai_api_key:
    st.info("请输入API密钥")
if submit and not subject:
    st.info("请输入主题")
if submit and not video_long >= 0.1:
    st.info("视频时长要大于或等于0.1分钟")
if submit:
    with st.spinner(("AI正在思考中，请稍等...")):
        title, video = generator_script(subject,video_long,creativity,openai_api_key)
    st.success("视频脚本已生成")
    st.subheader("标题：")
    st.write(title)
    st.subheader("文本内容：")
    st.write(video)