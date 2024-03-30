# def salary(days):
#     return days*1000

# from datetime import datetime as dt
# print(dt.now())

# import random
# num=random.randint(1,20)
# print(num)

import requests
data=requests.get('https://v2.jokeapi.dev/joke/Programming,Pun?amount=10')
j=data.json()
amount=j['amount']
print(amount)
for i in range(1,amount):
    m=j['jokes']
    n=m[i]['type']
    if n=='single':
        print("Joke:",m[i]['joke'])
    else:
        print("QUES:",m[i]['setup'])
        print("ANS:",m[i]['delivery'])


