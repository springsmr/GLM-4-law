from langchain_openai import ChatOpenAI

glm = ChatOpenAI(
    temperature=0.1,
    # model="glm-3-turbo",
    model="glm-4",
    openai_api_key="你的 api key",
    openai_api_base="https://open.bigmodel.cn/api/paas/v4/"
)
