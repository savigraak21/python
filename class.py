# CLASS-IS BLUEPRINT OF AN OBJECT
# OBJECT- IS A REAL WORLD ENTITY
# class name-- is done in camelcasing

# class Car():
#     name="Tata Nano"
#     color='parrot'
#     seats=2
#     wheels=5
#     def start(self):
#         # functions inside a class is called method or behaviour
#         print("vroom vroom...")
# savi_ki_car=Car()
# print(savi_ki_car.seats)
# savi_ki_car.start()

# class Dog():
#     name="sheru"
#     breed="pug"
#     legs="4"
#     tail="1"
#     color="black"
#     # the below used is a constructor--- intializes an object 
#     def __init__(self,name,age):
#         print('hello tommy')
#         self.name=name
#         self.age=age
#         self.breed="german sphered"


#     def bark(self):
#         print('whoof whoof...')
# # dog_func=Dog()
# # print(dog_func.name)
# # dog_func.bark()
# tommy=Dog("tommy",2)
# sheru=Dog("sheru",8)
# print(tommy.name)
# print(sheru.name)


# class Car():
#     def __init__(self,name,Model):
#         self.name=name
#         self.Model=Model

#     def start(self):
#         print("Self start")
# suzuki=Car("Swift","VDI")
# BMW=Car("BMW","S-Series")
# print(suzuki.name)
# print(BMW.name)
# self--- refers to current object 

# class BankofBaroda():
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance

#     def Accountinfo(self):
#         print("Welcome to Bank of Baroda")
#     def Deposit(self):
#         print(self.balance) 
#     def Saving(self): 
#         print("you have sufficient balance") 
        
# User1=BankofBaroda("Savi",20000)
# User2=BankofBaroda("Jaskiran",0)
# print(User1.name)
# print(User2.name)
# print(User2.balance)
# User1.Deposit()
# User2.Saving()

# class BankofBaroda():
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
#         self.bank_name="Bank of Baroda"
#     def deposit(self,money):
#         self.balance=self.balance+money
#         print("The money added is ")
#     def withdraw(self,money):
#         if self.balance<money:
#             print("Low balance")
#         else:
#             self.balance=self.balance-money
#             return money
# bank=BankofBaroda('Savi',2000)
# print(bank.balance)
# bank.deposit(200)
# print(bank.balance)
# bank.withdraw(300)
# print(bank.balance)

# bank1=BankofBaroda("jaskiran",0)
# print(bank1.balance)
# bank1.deposit(10)
# print(bank1.balance)
# bank1.withdraw(11)
# print(bank1.balance)


# class Animals():
#     def __init__(self,name,age,voice,breed):
#             self.name=name
#             self.age=age
#             self.voice=voice
#             self.breed=breed
#     def message():
#         print("We love humans.")
# class petAnimals(Animals):
#       def msg2():
#             print("We are pet animals.")
# class WildAnimals(Animals):
#         def msg():
#             print("We are wild animals.")
# class AquaticAnimals(WildAnimals,Animals):
#       def msg1():
#             print("We live in sea..")
    
# animal=Animals('tommy',4,"whoof","pug")  
# print(animal.name)
# Animals.message()
# wild=WildAnimals('jackal',2,"woooo","wild")
# print(wild.name)
# WildAnimals.message()
# WildAnimals.msg()
# AquaticAnimals.msg1()
# AquaticAnimals.message()
# from the class where we access/inherit --- super class/parent class
# the class where inherited features / attribute are to be used is called - subclass/child class



# class restaurant():
#     Nameofrestaurant="Mr.Papdi"
#     No_of_tables=10
#     Menu_Items=["chat papdi","gol gappe","tikki","momos","dahi bhalla","samosa","lime juice","water","fruit chat","chilli pakora"]
#     Book_table=True
#     Table_reservations=0
#     customer_orders=[]
#     def add_items_menu(self):
#         New_item=[input()]
#         # items=[New_item]
#         restaurant.Menu_Items.extend(New_item)
#     def Book_tables(self):
#         Booking=int(input("The number of bookings."))
#         if Booking>3:
#             print("Limit exceeded")
#         else:
#             print("Thank you for your reservation "+f'You have booked {Booking} tables.')
#     def customer_order(self):
#         print("Welcome to the restrautant")
#         customer_demand=input().lower()
#         if customer_demand in restaurant.Menu_Items:
#             n=int(input("Enter Quantity"))
#             cust_order=[customer_demand+str(n)]
#             restaurant.customer_orders.extend(cust_order)
#             print("Thanks for ordering...")
#         else:
#                 print("sorry not available")

               
# customer=restaurant()
# customer.customer_order()
# customer.Book_tables()


# polymorphism---we attain by overiding
# MRO-method resolution order

# class animal():
#     eyes=2
#     type_of='pet'
#     legs=4
#     tail=True
#     def speak(self):
#         # this acts as abstract method 
#         print('we love humans')
#         # pass
#         # raise NotImplementedError('this is only for inheritance and override')
# class dog():
#     legs=4
#     def __init__(self,name,age,color):
#         self.name=name
#         self.age=age
#         self.color=color
#     def speak(self):
#         print("woof woof..."+f'i have {dog.legs} legs.'+f'my name is {self.name}')
# Animal=animal()
# Dog=dog("sheru",5,"pug")
# Dog.speak()
# Animal.speak()
# static variables-- class level attributes --- self.name/dog.name--ways to access class level attributes
# dynamic variable-- object level attribute 
# Abstract class are classes which can be inherited in other classes and can be used in them.
# class dog():
#     def __init__(self,name,age,color):
#         self.name=name
#         self.age=age
#         self.color=color
#     def speak(self):
#         print("woof woof...")
#     def __str__(self):
#         return f'My name is {self.name}'
#     def __len__(self):
#         return 5
# Dog=dog('Sheru',3,"Pug")
# name="Savi"
# print(name)
# print(len(Dog))


# class restaurant():
#     Nameofrestaurant="Mr.Papdi"
#     No_of_tables=10
#     Menu_Items=["chat papdi","gol gappe","tikki","momos","dahi bhalla","samosa","lime juice","water","fruit chat","chilli pakora"]
#     Book_table=True
#     Table_reservations=0
#     customer_orders=[]
#     def add_items_menu(self):
#         New_item=input("Enter new Item:")
#         restaurant.Menu_Items.append(New_item)
#     def Book_tables(self):
#         Booking=int(input("The number of bookings."))
#         if Booking>3:
#             print("Limit exceeded")
#             Booking=int(input("The number of bookings."))
#             print("Thank you for your reservation "+f'You have booked {Booking} tables.')
#         else:
#             print("Thank you for your reservation "+f'You have booked {Booking} tables.')
#     def customer_order(self):
#         print("Welcome to the restrautant")
        
#         while True:
#             customer_demand=input("Enter your demand...").lower()
#             n=int(input("Enter Quantity"))
#             if customer_demand in restaurant.Menu_Items:
#                 cust_order=[customer_demand+str(n)]
#                 restaurant.customer_orders.extend(cust_order)
#             elif(customer_demand  not in restaurant.Menu_Items):
#                 print("Sorry not in the menu.")
#                 customer_demand=input("Enter your demand...").lower()  
#                 n=int(input("Enter Quantity"))
#                 cust_order=[customer_demand+str(n)]
#                 restaurant.customer_orders.extend(cust_order)  
#             elif(customer_demand=="that's it"):
#                 print("Thanks for ordering")
#                 break 



                
# customer=restaurant()
# customer.Book_tables()
# # customer.add_items_menu()               
# customer.customer_order()



class restaurant():
    No_of_tables_available=10
    list_of_2seating_tables=[1,3,5,7]
    list_of_3seating_tables=[2,4,6,8]
    Menu={
        "food":{
        "Chat Papdi":20,
        "Tikki":30,
        "Momos":30,
        "Spring Roll":30,
        "Dahi Bhalla":45
        },
      "Drinks":{
            "lime soda":20,
            "Cold Drink":30,
            "Frappe":80,
            "Coffee":90

        }
}
    # def add_items(self,)


