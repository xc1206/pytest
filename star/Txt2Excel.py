# -*- encoding: utf-8 -*-
import xlwt #需要的模块
import os
 
def txt_xls(filename,xlsname):
    """
    :文本转换成xls的函数
    :param filename txt文本文件名称、
    :param xlsname 表示转换后的excel文件名
    """
    with open(filename,'r',encoding='gbk',errors="ignore") as f:
        xls=xlwt.Workbook()
        style=xlwt.XFStyle()
        font=xlwt.Font()
        font.name=u"宋体"
        font.height=220
        style.font=font
        #生成excel的方法，声明excel
        sheet = xls.add_sheet('sheet1',cell_overwrite_ok=True) 
        x = 0 
        while True:
            #按行循环，读取文本文件
            line = f.readline() 
            if not line: 
                break  #如果没有内容，则退出循环
            for i in range(len(line.split(','))):
                item=line.split(',')[i]
                sheet.write(x,i,item,style) #x单元格经度，i 单元格纬度
            x += 1 #excel另起一行
        xls.save(xlsname) #保存xls文件

if __name__ == "__main__" :
    dir="E:/py/files/csv"
    """ filename = ""
    xlsname  = ""
    txt_xls(filename,xlsname) """
    for filename in os.listdir(dir):
        xlsxname=filename.split(".")[0]+".xlsx"
        txt_xls(dir+"/"+filename,dir+"/"+xlsxname)