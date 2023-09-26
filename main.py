import info
import api

# 关卡选择
level = 1
# 设置Cookie，从浏览器复制
api.UserCookie = ""
api.headers = {"Cookie": api.UserCookie , "content-type": "application/x-www-form-urlencoded; charset=UTF-8"}
# 设置过关时间(秒)
api.SpendTime = 1

res = api.getExam(info.exams[level - 1])
stIds = res[0]
zid = res[1]
examRecord = res[2]
print(stIds)
print(zid)
print(examRecord)
n = 0
for i in range(5):
    anwser = info.answers[level - 1].get(stIds[i])
    if(anwser is None):
        print("请录入以下答案")
        print(stIds[i])
        print(api.getCorrectAnwser(stIds[i],zid,examRecord))
        break
    elif api.getAnwser(stIds[i],anwser,zid,examRecord):
        print("答对一题")
        n = n + 1
    else:
        print("检查以下答案")
        print(stIds[i])
        print(api.getCorrectAnwser(stIds[i],zid,examRecord))
        print("未知错误")
        break

if(n == 5):
    print("题目全部通过，尝试提交")
    api.getGameRole(zid,examRecord)
else:
    print("题目未全部通过，请重试")

