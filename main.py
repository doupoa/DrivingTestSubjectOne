from json import load
import os

data = load(open('q.json', "r", encoding='utf-8'))


def select(question):
    hasAnswer = False
    for i in data:
        if question in i["question"]:
            if i["answer"] == "A":
                option = i["itemsDescArray"][0]
            if i["answer"] == "B":
                option = i["itemsDescArray"][1]
            if i["answer"] == "C":
                option = i["itemsDescArray"][2]
            if i["answer"] == "D":
                option = i["itemsDescArray"][3]
            print(
                f"问题: {i['question']}\n答案: {i['answer']} - {option}\n技巧: {i['answerSkill']}\n")
            hasAnswer = True
    if not hasAnswer:
        print("没有找到任何结果\n")
        return


while True:
    try:
        question = input('\nquestion:')
        if question:
            os.system("cls")
            select(question)
        else:
            os.system("cls")
            print("题目不得为空\n")
    except:
        os._exit(1)
