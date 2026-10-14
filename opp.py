# Multiple Inheritance
'''
class Parent_1:
    "statement" 
class Parent_2:
    "Statement"
class Child(Parent_1, Parent_2):
    "Statement"


object = Child()'''

'''
class Dad:
    def Property(self):
        print("Home")


class Mom:
    def Food(self):
        print("Special Food")

class Child (Dad, Mom):
    def Happy(self):
        print("👩‍🦱")

c=Child()
c.Property()
c.Food()
c.Happy()
'''

'''class A:
    def one(self):
        print("*")

class B:
    def one(self):
        print("$")

class C(A,B):
    def one(self):
        super().one()
        B.one(self)
        print("@+#")

c=C()
c.one()'''
'''
class x:
    def __init__(self):
        print("X Clad Data")

class y:
    def __init__(self):
        print("Y class Data")
class Z(x,y):
    def __init__(self):
        super().__init__()
        y.
        print("X AND Y class Information")

c=Z()
'''
'''
class Person:
    def Details(self, Name, Age, Loc):
        self.n = Name
        self.a = Age
        self.l = Loc

    def Data (self):
        print(f'Person Name is {self.n}\n'
              f'Person age is {self.a}\n'
              f'Current Loc is {self.l}')

class Teacher:
    def Display(self,name , sub,total_hour_taken_class):
        self.name = name
        self.sub = sub
        self.time = total_hour_taken_class

    def Data(self):
        print(f'Teacher name is {self.name}\n'
              f'Subject name is {self.sub}\n'
              f'Total Hour Of The Class {self.time}')
class Employee(Person, Teacher):
    def Information(self, sal, eid, role):
        self.sal=sal
        self.role= role
        self.eid = eid

    def Data (self):
        super().Data()
        Teacher.Data(self)
        print(f'Total salary of the employee {self.sal}\n'
              f'employee ID {self.eid}\n'
              f'Employee Role {self.role}')

e=Employee()
e.Details("Pranay", 23, "Pune")
e.Display("XYZ", "Excel", 2)
e.Information(600000, 101, "Data Analyst")
e.Data()
'''
'''
class Showroom1:
    def Bike(self,name, type):
        self.name = name
        self.type = type

    def show(self):
        print(f'Bike name is {self.name}\n'
              f'Bike Type is {self.type}')

class Car_Showroom:
    def Car_information(self, name, type):
        self.name = name
        self.type = type

    def show (self):
        print(f'Car Name is {self.name}\n'
              f'Car type {self.type}')

class Both_Information(Showroom1, Car_Showroom):
    def Information (self, color, model, type_engine):
        self.color = color
        self.model = model
        self.t = type_engine

    def show (self):
        super().show()
        Car_Showroom.show(self)
        print(f'Both car and Bike color {self.color}\n'
              f'Car And Bike Model is {self.model}\n'
              f'car and bike engine type {self.t}')

b= Both_Information()
b.Information("Red", "z1", "Electric")
b.Bike("Honda", 'Petrol')
b.Car_information("BMW", "Electric")
b.show()'''

'''
class Showroom1:
    def __init__(self,name, type):
        self.name = name
        self.type = type
        print(f'Bike name is {self.name}\n'
              f'Bike Type is {self.type}')

class Car_Showroom:
    def __init__(self, name1, type1):
        self.name = name1
        self.type = type1
        print(f'Car Name is {self.name}\n'
                      f'Car type {self.type}')

class Both_Information(Showroom1, Car_Showroom):
    
    def __init__ (self, name, type, name1, type1, color, model):
        super().__init__(self, name, type)
        Car_Showroom(self, name1, type1)
        self.color = color
        self.model = model
        print(f'Both car and Bike color {self.color}\n'
              f'Car And Bike Model is {self.model}')

b=Both_Information("Honda", "CD100", "BMW", "EV", "RED", "")

'''


class Student:
    def __init__(self, name):
        self.name =  name

    def display(self):
        print(f'Student name is {self.name}')

class Gamer:
    def __init__(self, game_name, level):
        self.gn = game_name
        self.l = level

    def show(self):
        print(f'game name is {self.gn}'
              f'game level {self.l}')

class ProGamer(Student, Gamer):
    def __init__(self, name, game_name,level, Rank):
        Student.__init__(self, name)
        Gamer.__init__(self, game_name, level)
        self.rank = Rank

    def Final(self):
        print(f'Game Rank is {self.rank}')

x=ProGamer("FreeFire", 'Bronze', "Gold", 1)
x.Final()