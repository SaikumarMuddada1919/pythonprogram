# -*- coding: utf-8 -*-
"""for loop  and patterns ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TKQ67HhOZLkSDjZaay-X33tG6I8TlaYc
"""

m=input()
n=m.split(",")
num=len(n)
for i in range(num):
    n[i]=int(n[i])
n=sorted(n)
print(n)

n=input()
k=int(input())
num_list=n.split(",")
n_l=len(num_list)
for i in range(n_l):
    num_list[i]=int(num_list[i])
num_list=sorted(num_list)
#max_sec=num_list[k]
print(num_list)



number=10
for i in range(1,number+1):
    print(i)

number=20
for i in range(1,number+1):
    if i%2==0:
        print(i)

numbers=100
sum=0
for i in range(1,numbers+1):
    sum+=i
print(sum)

list_a=['sai','rahul']
for i in list_a:
    print(i)

string='sai','rahul'
list_chr=list(string)
print(list_chr)

string="sai","rahul","shiva"
for i in string:
    print(i)

numbers=100
product=1
for i in range(1,numbers+1):
    product*=i
print(product)

unit=int(input('units='))
if 1<unit<100:
    print(10*unit)
elif 100<unit<200:
    print(15*unit)
elif 200<unit<300:
    print(15*unit)
else :
    print(20*unit)

n=input()
index=int(input())
m=n.split(",")
for i in range(len(m)):
    m[i]=int(m[i**2])
sum_n=sorted(m)
index_n=sum_n[index]
print(index_n)

n=input()
m=n.split(",")
index=[]
for i in len(m):
    index+=[int(m)**2]
print(m)

n=input()
index=int(input())
m=n.split(",")
for i in range(len(m)):
    m[i]=int(m[i])
sum_min=sorted(m)
sum_max=sorted(m, reverse=True)
print(sum_max)
index_n=sum_min[1]+sum_max[1]
print(index_n)

n=5
for i in range(n):
    print("*"*n)

n=5
for i in range(n+1):
    print("*"*i)

n=5
for i in range(n+1):
    print(str(i)*i)

n=5
for i in range(n+1):
    count=""
    for j in range(i):
        m=str(n-i)*(n-i)
        count=count+str(i)
    print(m)

n=5
for i in range(n):
    count=""
    for j in range(1,(n+1)-i):
        count=count+str(j)
    print(count)

n=5
for i in range(n+1):
    print("*"*i)
for j in range(n+1):
    m=("*")*(n-j)
    print(m)

n=10
for i in range(1,n+1):
    if i%2 != 0:
        print("*"*i)
for j in range(1,n+1):
    if j%2 != 0:
        m=("*")*(n-j+1)
        print(m)

n=5
counter=" "
for i in range(n+1):
    print(counter)
    counter=counter+