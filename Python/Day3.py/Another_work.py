#Made By Punit

=================== x x x x x x x x ===================

#Importing From Other Folder

import person #importing other file

print(person.greet("Punit"))

=================== x x x x x x x x ===================

#Random Module

import random

print("Random number between 1-100 : ", random.randint(1,100))
colors = ["red", "grey", "violet"]
print("Random color: ",random.choice(colors))

=================== x x x x x x x x ===================

#Date And Time Module

import datetime

today = datetime.date.today()
print("Today's date:", today)

now = datetime.datetime.now()
print("Current time:", now)

=================== x x x x x x x x ===================

#Sys Module

import sys

print("Python version:", sys.version)
print("Platform:", sys.platform)

=================== x x x x x x x x ===================

#Math Module

import math

print("Square root of 49:", math.sqrt(49))
print("value of pi:", math.pi)
print("Ceil of 6.9:", math.ceil(6.9))
print("Floor of 9.8", math.floor(9.8))
print("Power of 8'2", pow(8,2))

=================== x x x x x x x x ===================

#task
#create a function take random value using random Module
#check if the value is positive or negative and print it 
#check if the value is divisible with 5 or not and print it
#check if the value is odd or even

=================== x x x x x x x x ===================

import random

def num():
    x= random.randint(-10,10)
    print("random no. is :",x)
    if x >= 0:
        print("number is positive")
    else:
        print("number is negative")

    if x % 5 == 0:
        print("number is divisible by 5")b
    else:
        print("number is not divisible by 5")

    if x % 2 ==  0:
        print("number is even")
    else:
        print("number is odd")
num()

=================== x x x x x x x x ===================

#Class : is an blueprint for creating objects
#Object : ia an instance of a class 

=================== x x x x x x x x ===================

#Calculator

class Calculator:
    def add(self,a,b):
        return a+b
calc=Calculator()
print(calc.add(5,3))

 class abc:
   def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = abc("Punit", 18)
print(p1.name,p1.age)
print(p1.age)

=================== x x x x x x x x ===================

class Person:
  x=5
a = Person()
print(a.x)  

=================== x x x x x x x x ===================

class Person:
  def __init__(self, name, age):
        self.name = name
        self.age = age

  def greet(self):
       print(f"My name is {self.name} and I am {self.age} years old")
result=Person("Punit",18) 
result.greet()

=================== x x x x x x x x ===================

#Make A Calculator Using Class

class Calculator:
  def add(self, a, b):
    return a + b

   
  def subtract(self, a, b):
    return a - b

  def multiply(self, a, b):
    return a * b

  def divide(self, a, b):
    if b == 0:
      return "Error: Division by zero!"
      return a / b

    @staticmethod
    
    def main():
        calc = Calculator()
        while True:
            print("\nOperations:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '5':
                print("Exiting Calculator. Goodbye!")
                break

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", calc.add(num1, num2))
            elif choice == '2':
                print("Result:", calc.subtract(num1, num2))
            elif choice == '3':
                print("Result:", calc.multiply(num1, num2))
            elif choice == '4':
                print("Result:", calc.divide(num1, num2))
            else:
                print("Invalid choice! Please select a valid operation.")


# Run program
Calculator.main()

=================== x x x x x x x x ===================

#Made By Punit
