from Interface_Yss.Common.Base_Request import Base_requests
from Interface_Yss.project.user import userProject

re = Base_requests()
user = userProject(environment='online')
stu_data = {
    "loginName": 'haitun2',
    "password": "Test1234"
}
stu_res = user.stuLogin(data=stu_data)
ticket = stu_res['ticket']

url = 'https://user.artstudent.cn/auth/student/qualify/verifyUserInfo.htm'
payload = {
    'enterProfPage': '+AND+1%3D1+--+',
    'ticket': ticket,
}
res = re.post(url=url, data=payload)

if __name__ == "__main__":
    print(res)
