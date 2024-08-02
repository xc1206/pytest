import webbrowser
import requests
import requests.exceptions
import os
import threading
import openpyxl
from multiprocessing.pool import ThreadPool
from PIL import Image
import io

def openurls(filePath):
    with open(filePath,'r') as f:
        for line in f.readlines():
            webbrowser.open(line)
def openImgs(path,destination,start):    
    with open(path,'r') as f:
        for line in f.readlines():
            try:
                r=requests.request("get",line)
                with open(destination+"/"+str(start)+".jpg",'wb') as f:
                    f.write(r.content)
                start+=1
            except requests.exceptions.SSLError:
                continue
    print("下载结束")
def createDir(path,filePath):
    with open(filePath,'rb') as f:
        for line in f.readlines():
            name=str(line,encoding='utf-8').replace('\r','').replace('\n','').replace('/','')
            os.mkdir(path+"/"+name)
        print("success")
def createDir2(path):
    dir1='错误'
    dir2='正确'
    for dir in os.listdir(path):
        os.mkdir(path+"/"+dir+"/"+dir1)
        os.mkdir(path+"/"+dir+"/"+dir2)
    print("success")
def normPath(path):
    return os.path.normpath(path)
def renameFiles(org,des):
    for i in os.listdir(org):
        for j in os.listdir(des):
            os.rename(des+os.sep+j,des+os.sep+i)
def threadbase(url,name,destination):
    r=requests.request("get",url)
    if r.status_code==200:
        image=Image.open(io.BytesIO(r.content))
        image.save(destination+"/"+str(name)+".jpg")
    else:
        pass
def download_img(destination,download_xlsx,column):
    wb=openpyxl.load_workbook(download_xlsx)
    sheet=wb.active
    cells=sheet[column]
    threads=[]
    for cell in cells:
        url=cell.value
        name=cell.row
        thread=threading.Thread(target=threadbase,args=(url,name,destination))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    print('success')
if __name__=='__main__':
    # print("shit")
    destination=r'D:\job\0703sd'
    path="E:/py/files/txt/img.txt"
    start=2
    openImgs(path,destination,start)
    # path="D:/job/collection/其他配饰"
    # path='D:\job\collection\汽车配件'
    # filePath="E:/py/files/txt/file.txt"
    # createDir(path,filePath)
    # createDir2(path)
    # print(normPath(path))
    # org='D:\job\熊诚\og'
    # des='D:\job\熊诚\sl'
    # renameFiles(org,des)
    # print(os.listdir(org))
    # path='D:\job\收集（自研）\绘画、DIY制作'
    # filepath='E:\py/files/txt/file.txt'
    # createDir(path,filepath)