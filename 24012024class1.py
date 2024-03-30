# import random
# print("hello World",2)
# my_name='savi'
# age=21
# print(my_name," ",age)

# add 2 numbers
# Num_1=10
# Num_2=20
# result=Num_1+Num_2
# print('The result is:',result)

# # Area of circle
# radius=12
# pie_value=3.14
# area=pie_value*radius*radius
# print(area)

# swap the 2 numbers
# a=10
# b=30
# c=b
# b=a
# a=c
# print(a,b)

# a=11
# b=22
# a=a+b
# b=a-b
# a=a-b
# print(a,b)

# swap 2 numbers
# a=29
# b=92
# y=a%10
# x=int(a/10)
# a=(y*10)+x
# b=(x*10)+y
# print(a,b)

# Strings
# text='savi graak'
# # # print(text)
# # print(text[3]) #to select a particular letter through indexing
# # print(text[-2]) # negative indexing
# # print(text[0:4])
# print(text[-4:])
# # print(text[0:14:2]) #using stepsize
# print(text.capitalize())# for the first letter of 
# print(text.title()) # to captalize first letter of all the words in a string.
# print(text.count('a')) #this function is case-sensitive can count word and letter
# print(text.lower())
# print(text.upper())
# print(text.replace('v','V',1)) #last you can give the count of how many values you want to replace
# print(text.find('a',4)) # gives the index value of the first matching value , you can also mention to calculate after 4th index.
# text='hello,Welcome'
# print(text.casefold())
# print(text.center(20))
# print(text.encode())
# print(text.endswith('a'))
# print(text.expandtabs(2))

# text1='car'
# text2='table'
# text3=text1.replace(text1[0:2],text2[0:2])
# text4=text2.replace(text2[0:2],text1[0:2])
# print(text3,text4)

# take input from user /typecasting- changing one datatype to another/ float() int() str()  eval()- detects data type ,works only in case of float and
# num1=int(input("enter num1:"))
# num2=int(input("enter num2:"))
# sum=num1+num2
# print("The sum is:",sum)
# print(type(num1),type(num2))

# Text="Savi"
# age=21
# a=f"my name is {Text} and my age is {age}"
# print(a)
# print(len(Text))

# Last index of string without using negative index
# name=input("Enter your name:")
# print(f"last character of name is {name[-1]}")
# print(name[len(name)-1])
# name=input("Enter string:")
# name=name[:2].capitalize()+name[2:].capitalize()
# print(name)


# conditional statements
# age=int(input("Enter your Age:"))
# # if age>=18:
# #     print("you can vote.")
# # else:
# #     print("you cannot vote.")
# if age<=5:
#     print("Infant")
# elif age>=5 and age<=10:
#     print("Child")
# elif age>=10 and age<=18:
#     print("Teenager")
# elif age>=18 and age<=25:
#     print("Adult")
# else:
#     print("Senior Citizen")
# password=input("Enter password:")
# if password=="123@123":
#     print("login")
# else:
#     print("Oops!!! Try again.")

# check even odd
# num=int(input("Enter num:"))
# if num%2==0:
#     print("even")
# else:
#     print("odd")

# unit=int(input("Enter units consumed:"))
# if unit<100:
#     print("no dues.")
# elif unit>=200:
#     price=100*5+((unit-200)*10)
#     print(price)
# elif unit>=100:
#     price=(unit-100)*5
#     print(price)

#QUESTION
# name=input("enter your name:")
# bp=int(input("enter basic pay:"))
# pf=bp*(12/100)
# hra=bp*(20/100)
# if bp<300000:
#     da=bp*(20/100)
# else:
#     da=bp*(30/100)
# if hra>2000:
#     grosspay=bp+da+2000-pf
# else:
#     grosspay=bp+da+hra-pf
# netpay=grosspay-pf
# print(grosspay)
# print(netpay)

# nested if else
# username=input("enter your name:")
# password=input("enter password:")
# if username=="savi" and password=='123':
#     print('login')
# else:
#     print("try again")
 
# character=input("Enter character")
# # if character=='a' or character=='e' or character=='i' or character=='u':
# #     print('vowel')
# # else:
# #     print('consonent')
# if len(character)==1:
#     if character.isalpha():
#         if character in 'aeiou' or character in 'AEIOU':
#             print("Vowel")
#         else:
#             print("Consonant")
#     else:
#         print("Invalid character")
# else:
#     print("Enter single character")

# to check if leap year
# year=int(input("Enter year:"))
# if year%400==0 or year%100!=0 and year%4==0:
#     print('leap year')
# else:
#     print("Not a leap year")

# convert temprature from celcius to farhenheit
# Temp=eval(input("Enter Temprature in celcius:"))
# Temp= (Temp*9/5)+32
# print(Temp)

# # Convert farhenheit to celcius
# Temp1=eval(input("Enter temprature in Farhenheit:"))
# Temp1=(Temp1-32)*5/9
# print(Temp1)

# check if string palindrome
# Word=input("Enter Word:")
# if Word==Word[::-1]:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# list
# cars=['BMW','Nano','Maruti800']
# print(cars[1])
# use of random integer
# random_index=random.randint(0,2)
# option=['stone','paper','scissor']
# comp_choice=option[random_index]
# user_choice= input("Enter stone,paper,scissor:")
# if comp_choice==user_choice:
#     print("Computer Choice:",comp_choice)
#     print("Draw")
# elif comp_choice=='stone' and user_choice=='paper':
#     print("Computer Choice:",comp_choice)
#     print('User Wins')
# elif comp_choice=='stone' and user_choice=='scissor':
#     print("Computer Choice:",comp_choice)
#     print('Computer Wins')
# elif comp_choice=='paper' and user_choice=='stone':
#     print("Computer Choice:",comp_choice)
#     print('Computer Wins')
# elif comp_choice=='paper' and user_choice=='scissor':
#     print("Computer Choice:",comp_choice)
#     print('User Wins')
# elif comp_choice=='scissor' and user_choice=='paper':
#     print("Computer Choice:",comp_choice)
#     print('Computer Wins')
# elif comp_choice=='scissor' and user_choice=='stone':
#     print("Computer Choice:",comp_choice)
#     print("User Wins")

# month=input("Enter month:")
# if month in'January,March,May,July,August,October,Decemeber' or month in 'Jan,Mar,May,Jul,Aug,Oct,Dec' or month in 'jan,mar,may,jul,aug,oct,dec' or month in 'january,march,may,july,august,october,decemeber' :
#     print("Number of days is 31")
# elif month in 'February,Feb,feb,february':
#     print("Number of days is 28 in leap year 29")
# else:
#     print("Number of days is 30")

#  list
# cars=['BMW','Nano','Maruti800','Jeep','Ford']
# print(cars)
# print(cars[3])
# print(cars[-2])
# print(cars[-1][2])
# print(cars[2][:4])
# cars.append('Mercedes') inserts at last
# print(cars)
# cars.insert(3,'Mercedes') inserts at a specific position
# cars.pop(3) -- only takes index value
# cars.remove('Ford') -- removes string value
# cars.clear()-- clears the list
# cars.copy()-- copies the list
# cars.count()
# print(cars.count('Ford'))-- counts how many times a particular thing exsist
# print(len(cars))--- total number of items
# print(cars.index('Ford'))
# cars.sort()-- works on only homogenous data set
# cars.sort(reverse=True)
# cars.reverse()-- print in reverse order cars[::-1]
# sum()-- if list contains number it gives the sum of all the items in the list
# print(cars)
# marks=[
#     [45,65,56,64,76,"Savi"]
# ]
# a=sum(marks[0][0:5])
# percentage=(a/500)*100
# print("Name:",marks[0][-1] ,"and" ,"Percentage:",int(percentage))
# s='#'.join(cars) converts list to string
# print(s)

# lst=[6,2,5,9,7,3]
# n=6
# if n in lst:
#      k=lst.index(6)
#      l=lst.index(9)
#      a=sum(lst[0:n])-sum(lst[k:l+1])
#      print("sum is:",a)
     
# if n not in lst:
#     a=sum(lst[0:])
#     print("sum is:",a)

# tuples
# a=(1,2,3,4,5,4,6,7,8,9,4)
# print(a.count(4))
# print(a.index(3))

# Sets
# fruits={'apple','banana','cherry'}
# set2 = {"google", "microsoft", "apple"}
# fruits.add("orange")--add element in set
# fruits.clear()--- clears the set
# a= fruits.copy()-- creates copy of the set
# z=fruits.difference(set2)-- gives elements of fruits which are different from elements of set2 set.difference(fruits)-- gives the vice versa of the above
# print(z)
# fruits.difference_update(set2)-- removes the element which is common in both the sets
# fruits.discard("cherry")-- deletes the specified element
# z=fruits.intersection(set2)-- gives the common element between the two
# print(z)
# fruits.intersection_update(set2)--creates a set of the common element
# z=fruits.isdisjoint(set2)-- if there is no matching element in either set it returns true else it returns false
# print(z)
# print(fruits)
# x = {"a", "b", "c"}
# y = {"f", "e", "d", "c", "b", "a"}
# z = x.issubset(y) -- Checks if elements of x are present in y
# w=x.issuperset(y)--- checks if elements of y in x
# pop-removes any element from the set
#removes - removes a specified element from the set
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.symmetric_difference(y)-- returns elements in both set except the common ones
# x.symmetric_difference_update(y)--inserts the symmetric difference from y set to x set
#  union - returns all the elemnets in both the set
# update -- inserts elemnets from y to x
# print(x)

# print(z)
# print(w)

# # Panagram
# str=input()
# str=str.replace(" ","")  this coulb be optimized using if statement
# str=str.replace(".","")
# str=str.replace(",","")
# str=str.replace("!","")
# str=str.lower()
# str=set(str)
# alpha=set('abcdefghijklmnopqrstuvwxyz')
# x=str.difference(alpha)
# y=alpha.difference(str)
# if x==y:
#     print("Panagram")
# else:
#     print("Not a Panagram")

# dictionery
# population={
#     'USA':1234,
#     'IND':3456,
#     'CHI':4567,
#     'SRI':7890,
#     'L':{
#         'ABC':123
#     }
# }
# print(population)
# print(population['SRI'])
# print(population['L']['ABC'])

# d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
# print(d['k1'])
# print(d['k1'][2]['k2'][1]['tough'][2])

# loops

#While loop
# username=input("ENTER NAME:")
# password=input("ENTER PASSWORD:")
# signal='red'
# while signal!='green':
#     if username=='Savi' and password=='123':
#         print("login")
#         # signal='green'
#         break
#     else:
#         print("Invalid password")
#         username=input("ENTER NAME:")
#         password=input("ENTER PASSWORD:")

# chr=input()
# while True:
#     if chr.isalpha() and len(chr)==1:
#         print(chr)
#         chr=input()
#         break
#     else:
#         break

# random_index=random.randint(0,2)
# option=['stone','paper','scissor']
# comp_choice=option[random_index]
# user_choice= input("Enter stone,paper,scissor:")
# while True:
#     if user_choice=='E'or user_choice=='e':
#         break
#     if comp_choice==user_choice:
#         print("Computer Choice:",comp_choice)
#         print("Draw")
#         user_choice= input("Enter stone,paper,scissor:")
#     elif comp_choice=='stone' and user_choice=='paper':
#         print("Computer Choice:",comp_choice)
#         print('User Wins')
#         user_choice= input("Enter stone,paper,scissor:")
#     elif comp_choice=='stone' and user_choice=='scissor':
#         print("Computer Choice:",comp_choice)
#         print('Computer Wins')
#         user_choice= input("Enter stone,paper,scissor:")
#     elif comp_choice=='paper' and user_choice=='stone':
#         print("Computer Choice:",comp_choice)
#         print('Computer Wins')
#         user_choice= input("Enter stone,paper,scissor:")
#     elif comp_choice=='paper' and user_choice=='scissor':
#         print("Computer Choice:",comp_choice)
#         print('User Wins')
#         user_choice= input("Enter stone,paper,scissor:")
#     elif comp_choice=='scissor' and user_choice=='paper':
#         print("Computer Choice:",comp_choice)
#         print('Computer Wins')
#         user_choice= input("Enter stone,paper,scissor:")
#     elif comp_choice=='scissor' and user_choice=='stone':
#         print("Computer Choice:",comp_choice)
#         print("User Wins")
#         user_choice= input("Enter stone,paper,scissor:")

# i=1
# n=int(input())
# while(i<=n):
#     print("Savi",i)
#     i+=1
# i=1
# n=int(input())
# m=int(input())
# while(i<=m):
#     print(n,"x",i,"=",i*n)
#     i+=1
    
# i=1
# a=int(input())
# while (i<=a):
#    if (i%3==0 and i%5==0):
#       print("Fizzbuzz")
#    elif i%5==0:
#       print("Buzz")
#    elif i%3==0:
#       print("Fizz")
#    else:
#       print(i)
#    i=i+1

# n=int(input())
# ans=0
# binary=[]
# while(ans!=1):
#     ans=n//2
#     rem=n%2
#     binary.append(str(rem))
#     n=ans
# binary.append(str(ans))
# print("".join(binary[::-1]))

# sum of first 20 even numbers
# i=1
# sum=0
# n=int(input())
# while i<=n:
#     if i%2==0:
#         sum=sum+i
#     i=i+1
# print("sum is:",sum)
    
# factorial 
# n=int(input())
# if n==0:
#     print("The factorial is:",1)
# else:
#     fact=1
#     count=1
#     while count<=n:
#         fact=fact*count
#         count+=1
#     print("The factorial is:",fact)

#fibonacci series 
# n=int(input())
# a=0
# b=1
# print(a,b,end=' ')
# count=0
# t = 1
# while count<=n-2:
#     next_num=a+b
#     t = t + next_num
#     print(next_num,end=" ")
#     a=b
#     b=next_num
# count+=1
# print(t)

# prime numbers
# n= int(input()) 
# if n==2:
#     # print("Prime")
#     print(n)
# elif n%2==0:
#     pass
#     # print("Not Prime")
#     
# else:
#     is_prime=True
#     count=3
#     while count<n:
#         if n%count==0:
#             print("Not Prime")
#             is_prime=False
#             break
#         count=count+2
#     if is_prime==True:       
#         print("Prime")


   
# print prime numbers from 1 to 100
# n=int(input())
# prime=[]
# for i in range(0,n+1):
#     if i==0 or i==1:
#         continue
#     else:
#         for j in range(2,int(i/2)+1):
#             if i%j==0:
#                 break
#         else:
#             prime.append(i)
# print(prime)

# print even numbers 
# n=int(input())
# for i in range(1,n+1):
#     if i%2==0:
#         print(i)

# print odd numbers
# n=int(input())
# for i in range(1,n+1):
#     if i%2!=0:
#         print(i)  

# cars=['BMW','Ford','Nishan','Mustang','Toyota','Hundai']
# count=0
# while count<len(cars):
#     print(cars[count][0])
#     count+=1

# websites=['www.netmax.in','www.punjabicodex.in','www.google.com','www.yahoo.com','www.navy.gov.in',]
# count=0
# while count<len(websites):
#     site=websites[count]
#     i=site.find('.',4)
#     print(site[i:])
#     count+=1

# marks=[
#     [34,23,56,87,98,'Vishal'] ,
#     [54,87,88,90,68,'Jagdeep'],
#     [56,87,38,90,78,'Nisha'],
#     [57,87,34,92,78,'Ballu'],
#     [50,87,38,90,58,'Nikita']
# ]
# result=[]
# count=0
# result2=[]
# while count<len(marks): 
#     a=sum(marks[count][0:5])
#     percentage=(a/500)*100
#     result=[int(percentage),marks[count][-1]]
#     # result.append(int(percentage))
#     # result.append(marks[count][-1])
#     # print("Name:",marks[count][-1] ,"and" ,"Percentage:",int(percentage))
#     result2.append(result)
#     count+=1
# print(result2)

# for loop 
# n=int(input())
# for i in range(1,n+1,1):
#     print(i)
#     i+=1
# result=[]
# for i in range(0,len(marks)):
#     total=sum(marks[i][:-1])
#     percentage=total/500*100
#     result.append([int(percentage),marks[i][-1]])
#     i+=1
# print(result)

# for student in marks:
#     total=sum(student[:-1])
#     percentage=total/500*100
#     result.append([int(percentage),student[-1]])
# print(result)

#  prime number
# n =int(input())
# if n==0 or n==1 or n%2==0:
#     print("Not prime")
# elif n==2:
#     print("not prime")
# else:
#     is_prime=True
#     for i in range(3,n,5):
#         if n%i==0:
#             is_prime=False
#             print("not prime")
#             break
#     if is_prime==True:
#         print("Prime")

# players=['Sachine','Sehwag','Gambhir','Dravid','Raina']
# Scores=[100,15,17,28,43]
# combine={}
# for name in range(len(players)):
#     combine[players[name]]=Scores[name] 
#         # combine=dict(zip(players,Scores))
# print(combine)
print(format(145,'o'))




    








          
    
        
        




    
 
    




 
 


