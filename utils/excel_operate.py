# -*- coding:utf-8 -*- 
import sys
import os
import xlrd
import xlwt
from xlutils.copy import copy
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parentdir)

# book = xlwt.Workbook()
# sheet = book.add_sheet('xiangxin')
# # sheet.write(0,0,'name')  #行,列,内容

# #写入表内容
#         sheet.write(l, c, dd)
# #保存
# book.save('嵌套循环.xls')
########################################################################
class rd_excel:
    """"""
    #----------------------------------------------------------------------
    def __init__(self,sheet_name,exl_f_path):
        """"""
        self.sheet_name = sheet_name
        excel_file = exl_f_path
        self.excel_oper = xlrd.open_workbook(excel_file)
        self.sheet = self.excel_oper.sheet_by_name(sheet_name)
        
    #----------------------------------------------------------------------
    def get_sheet(self):
        """"""
        return self.sheet
    
    #----------------------------------------------------------------------
    def get_lines_cnt(self):
        """"""
        return self.sheet.nrows
        
    #----------------------------------------------------------------------
    def get_cell_value(self,row,col):
        """"""
        return self.sheet.cell_value(row,col)
        
    #----------------------------------------------------------------------
    def get_row_data(self,row_num):
        """"""
        return self.sheet.row_values(row_num)
        
    #----------------------------------------------------------------------
    def get_col_data(self,col_num):
        """"""
        return self.sheet.col_values(col_num)



class wt_excel:
    def __init__(self,sheet_name,exl_f_path):
        self.exl_f_path = exl_f_path
        self.book = xlwt.Workbook()
        self.sheet = self.book.add_sheet(sheet_name)
        
    def wt_cell(self,row,col,content):
        """写入单元格"""
        try:
            self.sheet.write(row,col,content)
            self.book.save(self.exl_f_path)
        except:
            raise "write into cell failed !!!"

        
if __name__ == '__main__':
    # excel = excel_obj("Sheet1",r"D:\workfile\zhongkeyuan_workspace\Attendance_sys_CQZGH\utils\t1.xls")
    # print(excel.sheet.__dict__ )

    # book = xlwt.Workbook()
    # sheet = book.add_sheet('xiangxin')
    # sheet.write(0, 0, "dd")
    # book.save('嵌套循环.xls')

    # wt_excel = wt_excel("Sheet999",r"D:\workfile\zhongkeyuan_workspace\Attendance_sys_CQZGH\mytest\analyse_sdk_script\result\t3.xls")
    # wt_excel.wt_cell(0,0,"HELLO")
    rd_xls = rd_excel("Sheet1",r"C:\Users\Administrator\IdeaProjects\sendmail\data\excel_case_manage.xlsx")
    con = rd_xls.get_col_data(0)
    print(con)