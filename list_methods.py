# -*- coding: utf-8 -*-
"""list methods.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SckvGIzv69kHvaRBeWyk1qIM3x-TeRRw
"""

a=[1,2,3]
b=[4,5,6]
a.extend(b)
print(a)

a=10
list_a=[]
for i in range(1,a+1):
    list_a.append(i)
    print(list_a)

a=[1,2,3]
b=4
a.insert(2,b)
print(a)

a=[1,2,3,4,5,6]
 b=4
 for i in range(b):
     a.pop()
     print(a)

a=[1,2,3]
b=4
a.append(b)
print(a)

n="saik8umar"
for i in n:
    if i=="8":
       continue
    print(i)

n="saik8umar"
for i in n:
    if i=="8":
       break
    print(i)

n='saikum4ar'
for i in n:
    if i.isdigit():
       continue
    print(i)

a=[1,2,3]
b=2
c=a.index(b)
print(c)

for i in range(6):
    pass

a=input()
b=[]
b.append(a)
print((b))

a=input()
counter=0
mode=0
for i in a:
    num=a.count(i)
    if num>counter:
        counter=num
        mode=i
print(mode)

a=[]
num_list=123
a.append(num_list)
a.insert(0,2)
a.append(1)
a.sort()
print(a)

n=5
num_list=[]
for i in range(n):
    command=input().split()
    if command[0]=="insert":
        num_list.command[0](command[1].command[2])
        print(num_list)

def fabboci(n):
    if n==1:
        return 1

    return (n-1)+(n-2)


n=int(input())
result=fabboci(n)
print(n)