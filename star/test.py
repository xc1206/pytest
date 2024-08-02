from turtle import *
import os
import pickle
import json
from queue import Queue
from collections import defaultdict
from urllib import request,parse
import ssl
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox
import re
import shutil
import pandas
import numpy
import openpyxl
import xlsxwriter
from PIL import Image
import threading
import pandas as pd
import numpy as np
from concurrent.futures import ThreadPoolExecutor
import math
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sbn


def my_trim(s):
    b=0
    t=len(s)-1
    while s[b]==' ':
        b+=1
    while s[t]==' ':
        t-=1
    return s[b:t+1]
def findMinAndMax(L):
    if L==None or L==[]:
        return
    return min(L),max(L)
def triangles():
    L=[1]
    while True:
        yield L
        L=[1]+[L[i]+L[i+1] for i in range(0,len(L)-1)]+[1]
def drawStar(x, y):
    pu()
    goto(x, y)
    pd()
    # set heading: 0
    seth(0)
    for i in range(5):
        fd(40)
        rt(144)
def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
def readFile(path):
    with open(path,"r") as f:
        return f.read()
def writeFile(path,str):
    with open(path,"a") as f:
        f.write(str)
def recur(basePath,keyword,res):
    pa=os.path
    jo=pa.join
    for item in os.listdir(basePath):
        if pa.isdir(jo(basePath,item)):
            recur(jo(basePath,item),keyword,res)
        if pa.isfile(jo(basePath,item)) and item.find(keyword)>=0:
            res.append(jo(basePath,item))
    # print(res)
    return res
def dup(obj,file):
    with open(file,'wb') as f:
        pickle.dump(obj,f)
def load(file):
    with open(file,'rb') as f:
        return pickle.load(f)
def minCoinMount(amount,coins):
    dp=[amount+1]*(amount+1)
    dp[0]=0
    #dp[i]=dp[i-coin]+1
    for i in range(len(dp)):
        for coin in coins:
            if i-coin>=0:
                dp[i]=min(dp[i],dp[i-coin]+1)
    return -1 if dp[amount]==amount+1 else dp[amount]
def permutate(nums):
    res=[]
    def trackback(start):
        if start==len(nums)-1:
            res.append(nums[:])
        for i in range(start,len(nums)):
            nums[start],nums[i]=nums[i],nums[start]
            trackback(start+1)
            nums[start],nums[i]=nums[i],nums[start]
    trackback(0)
    return res   
def subSets(nums,start):
    res=[]
    track=[]
    def trackback(track,nums,start):
        res.append(list(track))
        for i in range(start,len(nums)):
            track.append(nums[i])
            trackback(track,nums,i+1)
            track.pop()
    trackback(track,nums,start)
    return res
def subSetsV2(nums):
    res=[]
    track=[]
    def trackback(track,i):
        
        if i==len(nums):
            res.append(track[:])
            return
        trackback(track+[nums[i]],i+1)

        trackback(track,i+1)
    trackback(track,0)
    return res
def binarySearch(nums,target):
    left,right=0,len(nums)-1
    while left<=right:
        mid=left+(right-left)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            right=mid-1
        elif nums[mid]<target:
            left=mid+1
    return -2
def left_bound(nums,target):
    left,right=0,len(nums)
    while left<right:
        mid=left+(right-left)//2
        if nums[mid]==target:
            right=mid
        elif nums[mid]>target:
            right=mid
        elif nums[mid]<target:
            left=mid+1
    return left if nums[left]==target else -2
def right_bound(nums,target):
    left,right=0,len(nums)-1
    while left<=right:
        mid=left+(right-left)//2
        if nums[mid]==target:
            left=mid+1
        elif nums[mid]>target:
            right=mid-1
        elif nums[mid]<target:
            left=mid+1
    return left-1 if nums[left-1]==target else -2
def findAnagrams(s,t):
    win,need=defaultdict(int),defaultdict(int)
    for c in t:
        need[c]+=1
    left,right,valid=0,0,0
    res=[]
    while right<len(s):
        c=s[right]
        right+=1
        if c in need:
            win[c]+=1
            if win[c]==need[c]:
                valid+=1
        while right-left>=len(t):
            if valid==len(need):
                res.append(left)
            d=s[left]
            left+=1
            if d in need:     
                if win[d]==need[d]:
                    valid-=1
                win[d]-=1      
    return res
def lengthOfLongestSubstring(str):
    win={}
    left,right,res=0,0,0
    while right<len(str):
        c=str[right]
        right+=1
        win[c]=win.get(c,0)+1
        # while win[c]>1:
        #     d=str[left] 
        #     left+=1
        #     win[d]-=1
        while win[c]>1:
            d=str[left]
            left+=1
            win[d]-=1
        res=max(res,right-left)
    return res
def removeDup(nums):
    if not nums:
        return 0
    fast,slow=0,0
    pre=nums[slow]
    while fast<len(nums):
        if nums[fast]!=nums[slow]:
            slow+=1
            nums[slow]=nums[fast]
        fast+=1
    return slow+1
def removeEle(nums,target):
    if len(nums)==0:
        return 0
    slow,fast=0,0
    while fast<len(nums):
        if nums[fast]!=target:
            nums[slow]=nums[fast]
            slow+=1
        fast+=1
    return slow
def moveZeros(nums):
    slow,fast=0,0
    while fast<len(nums):
        if nums[fast]!=0:
            nums[slow]=nums[fast]
            slow+=1
        fast+=1
    for i in range(slow,len(nums)):
        nums[i]=0
def twoSum(nums,target):
    left,right=0,len(nums)-1
    while left<right:
        sum=nums[left]+nums[right]
        if sum==target:
            return left+1,right+1
        elif sum>target:
            right-=1
        elif sum<target:
            left+=1
    return -1,-1
def traverse(str):
    str=list(str)
    left,right=0,len(str)-1
    while left<right:
        tmp=str[left]
        str[left]=str[right]
        str[right]=tmp
        left+=1
        right-=1
    return "".join(str)
def isPalindrome(str):
    str=list(str)
    left,right=0,len(str)-1
    while str[left]==str[right] and left<right:
        left+=1
        right-=1
    return left==right
def longestPalindrome(str):
    str=list(str)
    res=""
    def inner(l,r):
        while l>=0 and r<len(str) and str[l]==str[r]:
            l-=1
            r+=1
        return str[l+1:r]
    for i in range(len(str)):
        s1=inner(i,i+1)
        s2=inner(i,i)
        res=s1 if len(s1)>len(res) else res
        res=s2 if len(s2)>len(res) else res
    return "".join(res)
def getModifiedArray(length,updates):
    diff=[0]*length
    def increase(i,j,val):
        diff[i]+=val
        if j+1<length:
            diff[j+1]-=val
    for update in updates:
        increase(update[0]-1,update[1]-1,update[2])
    res=[0]*length
    res[0]=diff[0]
    for i in range(1,length):
        res[i]=res[i-1]+diff[i]
    return res
def traverseSentence(str):
    str=list(str)
    def traverse(l,r):
        while l<r:
            tmp=str[l]
            str[l]=str[r]
            str[r]=tmp
            l+=1
            r-=1
    traverse(0,len(str)-1)
    l,r=0,len(str)-1
    for i in range(len(str)):
        if i==len(str)-1:
            if str[i]!=" ":
                r=i
                traverse(l,r)
        else:
            if str[i]!=" ":
                if str[i+1]==" ":
                    r=i
                    traverse(l,r)
            else:
                if str[i+1]!=" ":
                    l=i+1
                    # traverse(l,r)
    return str
def dupDir(path,destination):
    for f in os.listdir(path):
        os.mkdir(destination+"/"+f)
def removeFile(path):
    if os.path.isfile(path):
        os.remove(path)
    if os.path.isdir(path):
        for i in os.listdir(path):
            removeFile(path+"/"+i)
def simulateLogin():
    context=ssl._create_unverified_context()
    dic={
    'return_url':'https://biihu.cc/',
    'user_name':'xiaoshuaib@gmail.com',
    'password':'123456789',
    '_post_type':'ajax',
}
    url='https://biihu.cc//account/ajax/login_process/'
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    data=bytes(parse.urlencode(dic),'utf-8')
    req=request.Request(url,data=data,headers=headers,method='POST')
    response=request.urlopen(req,context=context)
    print(response.read().decode('utf-8'))
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
def tryBS4():
    soup=BeautifulSoup(html_doc,'lxml')
    print(soup.title.string)
def mesgbox(path):
    dirs=os.listdir(path)
    i=0
    while i<len(dirs):
        
        j=len(os.listdir(path+os.sep+dirs[i]))
        if j>=50: 
            box=tk.Tk()
            box.wm_attributes('-topmost',1)
            messagebox.showinfo(dirs[i],"Enough!")
            i+=1
            box.mainloop()
            box.withdraw()
def addRe(path,re):
    for file in os.listdir(path):
        port=os.path.splitext(file)
        os.rename(path+os.sep+file,path+os.sep+port[0]+re+port[1])
def changeName(des,path,movepath):
    # path=os.path
    listdir=os.listdir
    desNames=listdir(des)
    i=0
    with open(path,'r') as f:
        for line in f.readlines():
            n=desNames[i]
            old=des+os.sep+n
            new=des+os.sep+line.replace('\n','')+os.path.splitext(n)[1]
            os.rename(old,new)
            shutil.move(new,movepath)
            i=i+1
    print("success")
def listName(path,count):
    li=[]
    res=[]
    for i in os.listdir(path):
        li.append(os.path.splitext(i)[0])
    for i in range(count):
        if str(i) not in li:
            res.append(i)
    return res
def writelistToFile(pa,path,count):
    numbers=listName(path,count)
    for n in numbers:
        writeFile(pa,str(n)+"\n")
def writeList(pa,path):
    for i in os.listdir(path):
        writeFile(pa,os.path.splitext(i)[0]+"\n")
def exactPath(path,rgstr):
    os.path.split
def operate_xlsx(path,name,titles,content):
    os.chdir(path)
    wb=xlsxwriter.Workbook(name)
    ws=wb.add_worksheet()
    ws.write_row('A1',titles)
    ws.write_column('A2',content)
    wb.close()
def read_xlsx(path,name):
    os.chdir(path)
    wb=openpyxl.load_workbook(name)
    sheet=wb.active
    print('adresses such as below:')
    cells=sheet['A1:A10']
    for cell in cells:
        for j in cell:
            print(j.row," ",j.value)
def changeImageType(path,oldname,newtype):
    image=Image.open(path+os.sep+oldname)
    image.save(path+os.sep+os.path.splitext(oldname)[0]+"."+newtype,newtype)
def dowbload_imgs(des,download_file,col_name,named_by_url):
    df=pd.read_excel(download_file)
    df[col_name]=df[col_name].astype('str')+'?w=2000&h=1000'
    for i,url in enumerate(df[col_name]):
        try:
            # if not url is np.nan:
                r=requests.request("get",url)
                filename=''
                if named_by_url:
                    filename=os.path.basename(url.replace('?w=2000&h=1000',''))
                else:
                    filename=str(i+2)+".jpg"
                with open(des+"/"+filename,'wb') as f:
                    f.write(r.content)
        except requests.exceptions.MissingSchema:
            continue
    print("下载结束")
def download_imgs_by_async(func):
    with ThreadPoolExecutor(max_workers=4) as executor:
        for i in range(4):
            executor.submit(func)
def rename_column(path,oldname,newname,sheet_name='Sheet1'):
    df=pd.read_excel(path,sheet_name)
    df.rename(oldname,newname)
    print(df)
def replace_xlsx(old,new,path: str):
    for oldname in os.listdir(path):
        prefix_path=path+os.sep
        os.rename(prefix_path+oldname,prefix_path+oldname.replace(old,new))
def extract_postcode(xlsx_path):
    rg=r'(\d{5})'
    df=pd.read_excel(xlsx_path)
    for i,input in enumerate(df.input):
        df.at[i,'postcode']=re.findall(rg,input)
    df.to_excel(xlsx_path,index=False)
def create_changename_file(org,des,file):
    df=pd.DataFrame(os.listdir(org),columns=['org'])
    df1=pd.DataFrame(os.listdir(des),columns=['des'])
    pre=des+os.sep
    # df1['date']=[os.path.getctime(pre+file) for file in df1['des']]
    # df1.sort_values('date',inplace=True,ascending=True)
    # df1.reset_index(drop=True,inplace=True)
    # print(df1)
    df=df.join(df1)
    df.to_excel(file,index=False)
def change_name(file,des):
    df=pd.read_excel(file)
    pre_path=des+os.sep
    rec=re.compile(r'(.+)(\.\w+)')
    for i in df.index:
        old=df.at[i,'des']
        new=rec.match(df.at[i,'org']).group(1)+rec.match(df.at[i,'des']).group(2)
        os.rename(pre_path+old,pre_path+str(new))
def copy_file(file_xlsx,colname,org,des):
    df=pd.read_excel(file_xlsx)
    org_pre=org+os.sep
    des_pre=des+os.sep
    for name in df[colname]:
        shutil.copy(org_pre+name,des_pre+name)
def find_maxnum_indexs(nums):
    maxnum=10
    res=[]
    while maxnum not in nums:
        maxnum-=1
    for i,num in enumerate(nums):
        if num==maxnum:
            res+=[i+1]
    return res
def copy_file_from_word(org,des,word):
    df=pd.DataFrame(os.listdir(org),columns=['org'])
    org_pre=org+os.sep
    des_pre=des+os.sep
    for name in df['org']:
        if str(name).find(word)>=0:
            shutil.copy(org_pre+name,des_pre+name)
def create_column_by_func(func,xlsx,colname_old,colname_new):
    df=pd.read_excel(xlsx)
    # df[colname_new]=pd.Series(dtype=object,name=colname_new)
    df[colname_new]=df.apply(func,axis=1,args=(df,colname_old),raw=True)
    df.to_excel(xlsx,index=False)
def copy_file2(file,org,des,colname):
    df=pd.read_excel(file)
    org_pre=org+os.sep
    des_pre=des+os.sep
    for name in df['网址'][df[colname]==1]:
        name=os.path.basename(name)
        name1=os.path.splitext(name)[0]+'.png'
        shutil.copy(org_pre+name,des_pre+name)
        shutil.copy(org_pre+name1,des_pre+name1)
def rename_pre_by_after(des,after,pre):
    for name in os.listdir(des):
        pre1=os.path.splitext(name)[0]
        if after in name:
            name_new=pre1+pre+after
            os.rename(des+os.sep+name,des+os.sep+name_new)

def copy_selected_file(file_xlsx,colname,org,des):
    df=pd.read_excel(file_xlsx)
    org_pre=org+os.sep
    des_pre=des+os.sep
    for name in df[pd.notnull(df[colname])]['网址']:
        name=os.path.basename(name)
        shutil.copy(org_pre+name,des_pre+name)
def copy_file_from_dir(dir,org,des):
    org_pre=org+os.sep
    des_pre=des+os.sep
    for filename in os.listdir(dir):
        name=os.path.splitext(filename)[0]+'_sam'+'.png'
        shutil.copy(org_pre+name,des_pre+name)
def rename_file(file,des):
    df=pd.read_excel(file)
    image_names=df['原图']
    pre_dir=des+os.sep
    split_text=os.path.splitext
    for index,name in enumerate(image_names):
        name_tuple=split_text(name)
        realname=name_tuple[0]
        after=name_tuple[1]
        for des_file in os.listdir(des):
            changed_name=des_file.replace(realname,str(index+2))
            os.rename(pre_dir+des_file,pre_dir+changed_name)
def test():
    fruits=['banana', 'orange', 'mango', 'lemon', 'apple']
    print(fruits[::-1])

def work():
    # # re1="_sam"
    # re2='_shopline'
    # # path1=r'D:\job\zips\1sam\1sam'
    # path2="D:\job\zips\后缀"  
    # # addRe(path1,re1)
    # addRe(path2,re2)
    # path='D:\job\zips\pic_old-3'
    # pa='D:\job\zips/list.txt'
    # writeList(pa,path)
    # path=r'D:\job\pytest\test\changType'
    # name=r'自研模型效果评估对比（Shopify）06-27.xlsx'
    # titles=['序列号']
    # rdpath=r'D:\job\zips\pic_old-3'
    # content=[os.path.splitext(i)[0] for i in os.listdir(rdpath)]
    # operate_xlsx(path,name,titles,content)
    # read_xlsx(path,name)
    file_path=r'C:\Users\YY\Desktop\SD模型评分（0723-0730）.xlsx'
    des=r'D:\job\图片\0802sd'
    col_name='图片链接'
    # dowbload_imgs(des,file_path,col_name,named_by_url=True)
    download_imgs_by_async(dowbload_imgs(des,file_path,col_name,named_by_url=False))
    # rename_column(file_path,"address","网址")
    # path=r'D:\job\pytest\test\rename'
    # old='待标注'
    # new='标注完成'
    # replace_xlsx(old,new,path)
    # xlsx_path=r'D:\job\pytest\test\rename\addr_extract_MY_20240704_标注完成.xlsx'
    # extract_postcode(xlsx_path)
    # download_path=r'D:\job\pytest\test\downloadimgs\download.xlsx'
    # org=r'D:\job\zips\copy\org'
    # des=r'D:\job\zips\copy\des - 副本 - 副本 - 副本'
    # file=r'D:\job\pytest\test\listdir\list.xlsx'
    # create_changename_file(org,des,file)
    # change_name(file,des)
    # xlsx=r'C:\Users\YY\Desktop\concat_removebg_新增new.xlsx'
    # new='best'
    # old='熊诚'
    # # des=r'C:\Users\YY\Desktop\222.xlsx'
    # create_column_by_func(find_maxnum_indexs,xlsx,old,new)
    # pass
    # org=r'D:\job\zips\copy\org'
    # des=r'D:\job\zips\copy\cgq'
    # copy_file2(xlsx,org,des,'xc')
    # rename_pre_by_after(des,'.png','_new')
    # file=r'C:\Users\YY\Desktop\工作簿1.xlsx'
    # des=r'D:\job\zips\文字数据'
    # rename_file(file,des)

if __name__=="__main__":
    work()
    # test()