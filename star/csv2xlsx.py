import xlwt
import os

def transform(dir):
    
    for filename in os.listdir(dir):
        """ xls=xlwt.Workbook()
        sheet=xls.add_sheet("sheet1",cell_overwrite_ok=True) """
        with open(dir+"/"+filename,'r',errors='ignore',encoding="gbk") as f:
            with open(dir+"/"+filename.split(".")[0]+".xlsx",'w',encoding="gbk") as w:
                w.write(f.read())
if __name__=="__main__":
    dir="E:/py/files/csv"
    transform(dir)
    
