import random
import string
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re
import functools


def random_user_id(length):
    characters=string.ascii_letters+string.digits
    user_id=''
    for count in range(length):
        index=random.randint(0,len(characters)-1)
        character=characters[index]
        user_id+=character
    if len(user_id)==length:
        return user_id
    else:
        return None

def user_id_gen_by_user():
    length=input()
    count=input()
    length=int(length)
    count=int(count)
    for i in range(count):
        print(random_user_id(length))

def rgb_color_gen():
    rgb_lst=[]
    for i in range(3):
        rgb_lst+=[random.randint(0,255)]
    return f'rgb{tuple(rgb_lst)}'

def shuffle_list(lst):
    length=len(lst)
    if length==0:
        return lst
    for i in range(length//2):
        index=random.randint(0,length-1)
        changed_index=random.randint(0,length-1)
        tmp=lst[index]
        lst[index]=lst[changed_index]
        lst[changed_index]=tmp
    return lst

def set_of_seven_gen():
    array_set=set()
    length=0
    while length<7:
        num= random.randint(0,9)
        array_set.add(num)
        length=len(array_set)
    return array_set

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'

def list_comprehesion_test():
    # row=[]
    names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
    name_list=[' '.join(tpl) for row in names for tpl in row]
    print(name_list)

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

def say_hello():
    print('hello')

def higher_order_function():
    countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
    names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print(get_dictionary(countries))

def get_string_lists(lst):
    str_list=list(map(str,lst))
    return str_list

def get_dictionary(lst):
    lst_dic=dict()
    for l in lst:
        starting_letter=l[0]
        if starting_letter not in lst_dic:
            lst_dic[starting_letter]=len(list(filter(lambda x:x.startswith(starting_letter),lst)))
    return lst_dic

def datetime_test():
    # current date and time
    now = datetime.now()
    t = now.strftime("%m/%d/%Y, %H:%M:%S")
    print("time:", t)
    time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
    # mm/dd/YY H:M:S format
    print("time one:", time_one)
    time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
    # dd/mm/YY H:M:S format
    print("time two:", time_two)

def packing_and_unpacking_test():
    names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
    *nordic_countries,es,ru=names
    print(nordic_countries,es,ru)

def zip_test():
    fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
    vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
    fruits_and_veges = []
    for f, v in zip(fruits, vegetables):
        fruits_and_veges.append({'fruit':f, 'veg':v})

    print(fruits_and_veges)

def reg_ex_test():
    text='The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction'
    reg_ex_pattern=r'-?\d+'
    numbers=list(map(int,re.findall(reg_ex_pattern,text)))
    numbers.sort()
    distance=numbers[len(numbers)-1]-numbers[0]
    print(distance)
    # print(numbers)

def is_valid_variable(string):
    reg_ex_pattern=r'^[a-zA-Z][0-9a-zA-z_]*$'
    return re.match(reg_ex_pattern,string)!=None

def clean_text(sentence):
    pattern=r'[^\w\s]+'
    return re.sub(pattern,'',sentence)

def most_frequent_words(cleaned_text):
    words=cleaned_text.split(' ')
    lst=list(set([(words.count(word),word) for word in words]))
    lst.sort(reverse=True)
    return lst[:3]

def web_scraping():
    
    url = 'https://archive.ics.uci.edu/ml/datasets.php'

    # Lets use the requests get method to fetch the data from url

    response = requests.get(url)
    # lets check the status
    status = response.status_code
    print(status) # 200 means the fetching was successful

def getting_and_Knowing_your_data():
    url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv'
    crime = pd.read_csv(url, sep = ',')
    crimes = crime.resample('10AS').sum()

    # Uses resample to get the max value only for the "Population" column
    population = crime['Population'].resample('10AS').max()

    # Updating the "Population" column
    crimes['Population'] = population
    
    print(crime.idxmax(0))

def pandas_test():
    def func(lst):
        max_number = max(lst)
        return [index for index,number in enumerate(lst) if number==max_number]
    
    url = r'C:\Users\YY\Desktop\1.xlsx'
    address = pd.read_excel(url)
    address['input'] = address['input'].map(lambda x:x.split(','))
    # address['index'] = address['input'].map(lambda x:max(x))
    address['index'] = address['input'].map(func)
    
    # lst=address.loc[0,'input'].split(',')
    # print(type(address.loc[1,'index']))
    # print(type(address.loc[1,'input']))
    print(address)
    

if __name__ == '__main__':
    pandas_test()

    