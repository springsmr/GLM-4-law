import jsonlines
from tqdm import tqdm
from utils import read_jsonl

from agents.chat_router import route


def answer(query: str):
    agent = route(query)

    messages = agent.invoke({"messages": [("human", query)]})
    return messages


if __name__ == '__main__':
    question_file = "./data/questions/question.jsonl"
    # 修改输出文件
    result_file = "./data/results/伍柒_result.json"
    queries = read_jsonl(question_file)

    # 生成答案
    print("Start generating answers...")

    for query in tqdm(queries):
        # 如果中断，可以从这里开始
        if query["id"] < 76:
            continue
        response = answer(query["question"])
        content = {
            "id": query["id"],
            "question": query["question"],
            "answer": response["output"]
        }
        with jsonlines.open(result_file, "a") as json_file:
            json_file.write(content)
