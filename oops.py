# inheritance 

class Animal():
    eyes=2
    legs=4
    tail=True
    def msg(self):
        print("We are animals")

class Dog(Animal):
    def __init__(self,name,color,age):
        self.name=name
        self.color=color
        self.age=age
    def speak(self):
        print("whoof whoff")
sheru=Dog('sheru','white',4)
sheru.msg()
print(sheru.legs)