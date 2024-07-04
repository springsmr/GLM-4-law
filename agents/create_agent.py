from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

template_prompt = """
你是一个专业的信息检索员，擅长通过调用工具来检索信息，会通过调用工具来检索信息。
如果遇到比较复杂的复合问题，你可以先拆解成多个小问题，然后依次回答小问题，最后将多个小问题的答案组合起来回答整个问题。
如果遇到开放问题，你可以自由作答。
"""

company_prompt = """
你是一个擅长回答与公司有关的问题的专家，会通过调用工具来检索信息。
如果遇到比较复杂的复合问题，你可以先拆解成多个小问题，然后依次回答小问题，最后将多个小问题的答案组合起来回答整个问题。
如果遇到开放问题，你可以自由作答。
"""

law_prompt = """
你是一个擅长回答与法律有关的问题的专家，会通过调用工具来检索信息。
如果遇到比较复杂的复合问题，你可以先拆解成多个小问题，然后依次回答小问题，最后将多个小问题的答案组合起来回答整个问题。
如果遇到开放问题，你可以自由作答。
"""


def create_agent(llm: ChatOpenAI, tools: list, system_prompt: str = template_prompt):
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                system_prompt,
            ),
            MessagesPlaceholder(variable_name="messages"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )
    agent = create_openai_tools_agent(llm, tools, prompt)
    executor = AgentExecutor(agent=agent, tools=tools)
    return executor
