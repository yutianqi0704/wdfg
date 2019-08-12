
# coding: utf-8

# In[8]:


#第一题
#一个五角数被定义为n(3n-1)/2，编写一个测试程序使用这个函数显示前100个五角数。每行显示10个
def getPentagonalNumber(n):
    c = int(n * (3 * n-1) / 2)
    print(c,end='\t')
    if n % 10 ==0:
        print()
for i in range(1,101):
    getPentagonalNumber(i)


# In[7]:


#第二题
def sumDigits(n):
    a = n
    b = 0
#str 将括号中的内容强制转换为字符串
    for i in range(0,len(str(a))):
        if i<len(str(a)):
            e = n % 10
            n = n //10
        b = b + e
    print(b)
sumDigits(27953)


# In[6]:


#第三题
def desplaySortedNumbers(num1,num2,num3):
    print("Enter three number:",num1,num2,num3)
    if num1>num2 and num1>num3:
        if num2 > num3:
            print("The sorted number are",num3,num2,num1)
        else:
            print("The sorted number are",num2,num3,num1)
    elif num2>num1 and num2>num3:
        if num1 > num3:
            print("The sorted number are",num3,num1,num2)
        else:
            print("The sorted number are",num1,num3,num2)
    elif num3>num1 and num3>num2:
        if num1 > num2:
            print("The sorted number are",num2,num1,num3)
        else:
            print("The sorted number are",num1,num2,num3)
desplaySortedNumbers(56,89,21)


# In[23]:


#第四题
# 编写一个程序提示用户输入投资额和百分比格式的年利率，然后输出一份表格显示年份从1到30年的未来值。
def futureInvestmentValue(benjin,lilv,years):
    years = years+1
    for i in range(1,years):
        shouyi = benjin + benjin*lilv
        print(i,shouyi)
        benjin=shouyi
futureInvestmentValue(10000,0.09,30)


# In[7]:


#第五题
#打印ch1到ch2之间的字符，按每行指定某个数来打印。编写一个测试程序，打印“1”到“Z”的字符，每行打印10个
def printChars(ch1,ch2,num):
    q=ord(ch1)+1
    w=ord(ch2)
    n=0
    for i in range(q,w):
        n=n+1
        if n%num !=0:
            print(chr(i),end='  ')
        else:
            print(chr(i))
        
printChars('1','Z',10)


# In[8]:


#第六题
#编写一个程序测试，显示从2010年到2020年每年的天数
def numberOfDaysInAYrea(year):
    if year%100==0:
        if year%400==0:
            print(year,"366天")
        else:
            print(year,"365天")
    elif year%4==0:
        print(year,"366天")
    else:
        print(year,"365天")

for year in range(2010,2021):
    numberOfDaysInAYrea(year)


# In[9]:


#第七题
#计算两点间距离
import math
def distance(x1,y1,x2,y2):
    q=(x1-x2)**2
    w=(y1-y2)**2
    e=q+w
    dis= math.sqrt(e)
    print("两点间距离为：",dis)
    
distance(1,2,3,4)


# In[10]:


#第八题
#如果一个素数可以写成2**（P-1）的形式，其中p是某个正整数，那么这个数就被称作梅森素数。编写程序找出p<=31的梅森素数。
def meisen(p):
    q=pow(2,p)-1
    m=2
    if p==2:
        print(p,q)
    for i in range(2,p):
        m=m+1
        if p%i==0:
            break
        if m == p:
            print(p,q)
            
for p in range(1,32):
    meisen(p)


# In[1]:


#第9题
#调用time.time()返回1970年1月1日0点开始的毫秒数。
import time
print(time.time())
time = time.localtime(time.time())
print("Cuurrent date and time is",time.tm_year,"年",
      time.tm_mon,"月",time.tm_mday,"日",
      time.tm_hour,":",time.tm_min,":",time.tm_sec)


# In[6]:


#第十题
#(游戏，掷骰子)
import numpy as np
def dianshu():
    res1 = np.random.choice([1,2,3,4,5,6])
    print("您第一次抛出的点数为：",res1)
    res2 = np.random.choice([1,2,3,4,5,6])
    print("您第二次抛出的点数为：",res2)
    res = res1 + res2
    print("您抛出的两次点数之和为：",res)
    return res
res = dianshu()
if res==2 or res==3 or res==12: 
    print("您输了")
elif res==7 or res==11:
    print("您赢了")
else:
    res3 = res
    res = dianshu()
    if res==7 or res == res3:
        print("您赢了")
    else:
        print("请开下一局")


# In[9]:


import time
class Time(object):
    def __init__(self):
        self.time=time
    def shuzi(self):
        for i in range(1,100):
            i=i+1
            if i<100:
                time.sleep(1)
                now = time.localtime()
                print(time.strftime("%H:%M:%S \r",now),end="",flush=True)
                if time.strftime("%H:%M:%S",now)=='20.11.23':
                    print("闹钟响了")
                else:
                    pass
Time().shuzi()               

