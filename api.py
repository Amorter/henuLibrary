import requests
from bs4 import BeautifulSoup
UserCookie = ""
SpendTime = 1
headers = {"Cookie": UserCookie , "content-type": "application/x-www-form-urlencoded; charset=UTF-8"}


def getAnwser(stid,answer,zid,examRecord):
    params = "stid=" + stid + "&answer=" + answer + "&zid=" + zid + "&examRecordDetailsId=" + examRecord + "&spendtime=1&helpId=00000000-0000-0000-0000-000000000000"
    response = requests.post("http://hndxrgjy6.zhixinst.com/web/Exam/GetAnswer",data = params,headers = headers)
    return response.json().get('isCorrect')


def getExam(cid):
    response = requests.get("http://hndxrgjy6.zhixinst.com/Web/Exam?cid=" + cid,headers=headers)
    soup = BeautifulSoup(response.content,'html.parser')
    stIds = soup.find('input', id = 'stIds').get('value').split(',')
    zid = soup.find('input', id = 'zid').get('value')
    examRecord = soup.find('input', id = 'examRecordDetailsId').get('value')
    return stIds,zid,examRecord

def getCorrectAnwser(stid,zid,examRecord):
    params = "stid=" + stid + "&answer=de36480a-4765-44f3-ba1d-9d8e1863386f" + "&zid=" + zid + "&examRecordDetailsId=" + examRecord + "&spendtime=1&helpId=00000000-0000-0000-0000-000000000000"
    response = requests.post("http://hndxrgjy6.zhixinst.com/web/Exam/GetAnswer",data = params,headers = headers)
    return response.json().get('examQuestion').get('answer')

def getGameRole(zid,examRecord):
    params = "examRecordDetailsId=" + examRecord + "&zid=" + zid + "&spendtime=" + str(SpendTime)
    response = requests.post("http://hndxrgjy6.zhixinst.com/web/exam/GetGameRole",data = params , headers=headers)