# -*- coding: utf-8 -*-
# @Time : 2021/3/11 18:32
# @Author : dujun
# @describe : describe
# @File : case.py

import xlrd
from Interface_Yss.project.user import userProject


def read_excel():
    excel_list = []
    path = r'C:\Users\Administrator\Desktop\excel.xls'
    excel = xlrd.open_workbook(path)
    sheet_names = excel.sheet_names()
    sheet = excel.sheet_by_index(0)
    nows = sheet.nrows
    cols = sheet.ncols
    key = sheet.row_values(0)
    for i in range(1, nows):
        excel_dict = {}
        value = sheet.row_values(i)
        for j in range(0, cols):
            excel_dict[key[j]] = value[j]
        excel_list.append(excel_dict)
    print(excel_list)
    print(nows)
    return nows, excel_list


def send():
    user = userProject(environment='')
    data = read_excel()
    for i in range(0, data[0]-1):
        payload = {
            'loginName': data[1][i]['username'],
            'password': data[1][i]['password']
        }
        print(payload)
        re_stu = user.stuLogin(data=payload)
        print(re_stu)


if __name__ == "__main__":
    send()
