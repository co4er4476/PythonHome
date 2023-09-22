#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('Python --version')


# In[2]:


get_ipython().system('python --version')


# In[3]:


get_ipython().system('pwd')


# In[4]:


get_ipython().system('ls')


# In[5]:


get_ipython().system('ls -a')


# In[6]:


get_ipython().system('clear')


# In[7]:


get_ipython().system('cat test.dat')


# In[9]:


get_ipython().system('cat data.dat')


# In[23]:


fread = None
try :
    fread = open('data.dat', 'r')
    #1.
    #result = fread.read()
    #2.
    # result = fread.readline() #초기화    
    # while result :
    #     print(result, end='')
    #     result = fread.readline()

    for line in fread.readlines():
        print(line)
except :
    print('File Not Found')
finally :
    fread.close()


# In[26]:


poet = """
죽는날 까지 하늘을 우러러
한점 부끄럼이 없기를
잎새에 이는 바람에도
나는 괴로워 했다
별을 노래하는 마음으로
모든 죽어가는 것을 사랑해야지
그리고 나에게 주어진 길을
걸어가야겠다.
오늘밤에도 별이 바람에 스치운다
"""


# In[27]:


fwrite = None
try:
    fwrite = open('서시.txt', 'w') #write 방향, 즉 메모리에서 디스크 방향
    fwrite.write(poet) #write는 양과 무관하게 한번에 내용을 내보냄
    print("File Saved Successfully.")
except :
    print("File Not Found")
finally :
    fwrite.close()


# In[32]:


with open('서시.txt', 'rt') as fread :
    try :
        count = 0
        for line in fread.readlines() :
            print(f'{count}: {line}', end='')
            count += 1
    except :
        print("File Not Found")


# In[33]:


import json


# In[37]:


list_ = ['Hello, world', 39, True, 34.92]
type(list_)
str_ = json.dumps(list_)
type(str_)


# In[38]:


print(str)


# In[39]:


print(str_)


# In[41]:


obj = json.loads(str_)
type(obj)


# In[42]:


obj[2]


# In[48]:


student = {
"hakbun" : "20230902",
"name" : "nana",
"age" : 23,
"address" : "서울시 강남구"    
}
type(student)


# In[55]:


str1_ = json.dumps(student, ensure_ascii=False, indent='\t') #indent는 들여쓰기
type(str1_)
print(str1_)


# In[57]:


with open('student.dat', 'wt') as fwrite :
    fwrite.write(str1_)
    print("File Saved Successfully")


# In[67]:


with open('student.dat', 'rt') as fread :
    result = fread.read()
# print(type(result))
obj = json.loads(result)
# print(type(obj))
print(f"name = {obj['name']}, age = {obj['age']}")


# In[74]:


with open('sungjuk.json', 'rt') as fread :
    result = json.load(fread)
    print(type(result))
    print(result[0]['irum'])


# In[76]:


import os


# In[77]:


os.chdir('/')
print(os.getcwd())

!pwd
# In[80]:


import sys


# In[82]:


print(f"Version : {sys.version}")
print(f"Version Info: {sys.version_info}")
print(f"Platform : {sys.platform}")


# In[84]:


import platform


# In[88]:


print(f"OS name : {platform.uname()}")


# In[89]:


import socket


# In[90]:


print(f"Hostname : {socket.gethostname()}")


# In[92]:


hostname = socket.gethostname()
print(socket.gethostbyname(hostname))


# In[105]:


hostname = 'www.google.com'
print(socket.gethostbyname(hostname))


# In[111]:


get_ipython().system('pwd')


# In[112]:


get_ipython().system('cd ~')


# In[113]:


get_ipython().system('pwd')


# In[ ]:




