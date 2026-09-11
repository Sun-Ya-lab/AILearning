import json
josn_test = '''
{
    "question": "什么是RAG？",
    "answer": "RAG是检索增强生成。",
    "time": "2026-09-11 13:50:00"
}
'''
l = json.loads(josn_test)
def hanshu(s):
    qustion = l["question"]
    answer = l["answer"]
    time = l["time"]
def main():
    print(l)
if __name__ == '__main__':
    main()