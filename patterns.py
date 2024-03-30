# import modules
import summodule
# *
# **
# ***
# ****
# *****
# ******
# n=int(input())
# for i in range(1,n+1):
#     for j in range(i):
#         print("*", end='')
#     print()
# 1
# 22
# 333
# 4444
# 55555
# n=int(input())
# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end='')
#     print()

# 1
# 12
# 123
# 1234
# 12345
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()

# *****
# ****
# ***
# **
# *
# n= int(input())
# for i in range(n,0,-1):
#     for j in range(i)/(n-i):
#         print("*",end='')
#     print()

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# n=int(input())
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=' ')
#     print()
# for i in range(1,n+1):
#     for j in range(n-i):
#          print("*",end=' ')
#     print()
#     *
#    **
#   ***
#  ****
# *****
# n= int(input())
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end='')
#     for j in range(i):
#         print("*",end='')
#     print()

#     * 
#    * * 
#   * * * 
#  * * * *
# * * * * *
# n= int(input())
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end='')
#     for j in range(i):
#         print("* ",end='')
#     print()

# n=int(input())
# for i in range(1,n+1,2):
#     for k in range(n-i):
#         print(" ",end='')
#     for j in range(i):
#         if j==0 or j==i-1:
#             print("1 ",end='')
#         else:
#             print("0 ",end='')
#     print()

# functions
# def  hello():
#     print("Hello Savi")
# hello()

# def sum_of():
#     num1=int(input())
#     num2=int(input())
#     sum=num1+num2
#     print(sum)
# sum_of()

# def salary():
#     days=int(input())
#     salary= 10000*days
#     print(salary)
# salary()

# def salary(x):
#     days=x
#     salary= 10000*days
#     print(salary)
# no=int(input())
# salary(no)

# def even_odd():
#     num=int(input())
#     if num%2==0:
#         print("Even")
#     else:
#         print("Odd")
# even_odd()

# def salary(x):
#     days=x
#     salary= 10000*days
#     # print(salary)
#     return salary
# no=int(input())
# s=salary(no)
# print(s+1000)

# def countvowels_consonants(para):
#     vowels=0
#     consonants=0
#     para.lower()
#     for i in para:
#         if i in 'aeiou':
#             vowels=vowels+1
#         else:
#             consonants=consonants+1
#     return vowels,consonants
# para=input()
# s=countvowels_consonants(para)
# print(s)

# def salary(days):
#     return days*1000
# print(salary(20))

# sal=modules.salary(28)
# print(sal)

# import tcs.filename as v
# from tcs import filename as alias name    
sum=summodule.sum(2,4)
print(sum)








