from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

def generator_script(subject,long,creativity,api_key):
    title_template = ChatPromptTemplate.from_messages(
        [
            ("human","请为'{subject}'这个主题的视频想一个吸引人的标题")
        ]
    )

    video_template = ChatPromptTemplate.from_messages(
        [
            ("human",
                     """你是一位短视频频道的博主，使用中文并根据以下标题和相关信息，为短视频频道写一个视频脚本。
                     标题：{title}，视频时长：{long}，生成的脚本尽量遵循时间要求。
                     要求开通抓住眼球，中间提供干货内容，结尾有惊喜，脚本格式也请按照【开头，中间，结尾】分隔。
                     整体内容的表达方式要尽量轻松有趣，吸引年轻人。
                     """)
        ]

    )

    model = ChatOpenAI(openai_api_key=api_key, base_url="https://api.aigc369.com/v1", temperature=creativity )

    title_chain = title_template | model
    video_chain = video_template | model

    title = title_chain.invoke({"subject":subject}).content
    video = video_chain.invoke({"title":title, "long":long}).content

    return title,video

#print(generator_script("sora模型",1,0.7,"sk-HXNj6BThaabCNbmD17Aa628238374aB6A2Ac1fC60c47D4Ac"))