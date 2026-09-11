from datetime import datetime
'''
infor = dict()
name = input("请输入你的名字")
question = input("请输入问题：")
answer = input("请输入回答：")

record = {
        "question": question,
        "answer": answer,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
 }

infor[name] = record

print(infor)
'''
infor = dict()
strs = input("请输入你的名字、问题、回答,输入 q 结束\n")
while True:
    strs = strs.split(" ")
    print(strs)
    if strs[0] == "q":
        break
    record = {
        "question": strs[1],
        "answer": strs[2],
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    infor[strs[0]]=record
    strs = input("请输入你的名字、问题、回答,输入 q 结束\n")
print(infor)
list = [1,23,2]
print(list)






