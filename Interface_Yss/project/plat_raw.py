# -*- coding: utf-8 -*- 
# @Time : 2021/1/8 19:07 
# @Author : dujun
# @describe : describe
# @File : plat_raw.py 
from Interface_Yss.data import CommonData, VideoSchema_Data, Account
from Interface_Yss.data.caps import Caps
from Interface_Yss.Common.Base_Request import Base_requests


class platRaw:
    def __init__(self, environment):
        self.re = Base_requests()
        self.caps = Caps(env=environment)
        self.plat_data = VideoSchema_Data.platData()

    # 平台登录
    def plat_login(self, data=None):
        url = self.caps['college'] + '/login'
        if data is None:
            response = self.re.post(url=url, data=Account.yuanXiao)
            self.ticket = response['ticket']
        else:
            response = self.re.post(url=url, data=data)
            self.ticket = response['ticket']
        return response

    # 院校后台查询对应考试视频
    def schoolQueryVideo(self):
        url = self.caps['examVideo'] + '/auth/school/assignDetail/loadExaminerAssignDetailData.htm'
        datas = {
            "data": self.plat_data.schoolQueryVideo,
            "ticket": self.ticket
        }
        response = self.re.post(url=url, data=datas)
        return response

    # 创建考生
    def createStu(self, data=''):
        url = self.caps['user'] + '/auth/admin/user/saveUser.htm'
        response = self.re.post(url=url, data=data)
        return response