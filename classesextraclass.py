# class Car():
#     name='hyundai'
#     model='i20'
#     wheels=4
#     doors=4
# #properties/ attributes of cars
#     def start(self):
#         print('wrom wrom')
# car=Car()
# print(car.name)
# car.start()

# use of constructor
# constructor calls itself and assigns memory to variables and functions
# class Car():
#     def __init__(self,name,model,color):
#         self.name=name
#         self.model=model
#         self.color=color
#         self.doors=4
#         self.wheels=4
#         # print("hello")
# ford=Car('ford','xyz','blue')
# print(ford.name)

# class Animal():
#         legs=4
#         tail=1  
#         def __init__(self,breed,age,name):
#             self.breed=breed
#             self.age=age
#             self.name=name
            
#         def speak(self):
#             print(f'hello my name is {self.name}')
# dog=Animal('Pug','4','Sheru')
# dog.speak()
# print(dog.tail)


# polymorphism
# class Animal():
#     legs=4
#     eyes=2
#     def speak(self):
#         print("We are animals")
# class Dog(Animal):
#     def __init__(self,name,breed,color):
#         self.name=name
#         self.breed=breed
#         self.color=color
#     def speak2(self):
#         print("Whoof Whoof")

# dog=Dog('sheru','pug','black')
# dog.speak()

# Abstarct


# def shout(text): 
#     return text.upper() 
 
# print(shout('Hello')) 
 
# yell = shout 
 
# print(yell('hola')) 

s={"savi","22","abcd",1,True,2,5,6}
print(s)
