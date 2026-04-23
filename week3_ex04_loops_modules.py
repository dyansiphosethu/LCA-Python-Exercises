#Question 1: Using a loop with a list
fruits = ["apple", "banana", "kiwi", "orange", "mango"]

for item in fruits:
  print(item)
  
#Question 2: Using a while loop for countdown
counter = 5
while counter > 0:
  print(counter)
  counter -= 1
  
#Question 3: Using a for loop with range()
for index in range(1,11):
  print(index ** 2)
  
#Question 4: Using the random module
import random

colors = ["green", "red", "yellow", "blue", "white", "gold", "pink", "brown"]

for index in range(0, 3):
  print(colors[random.randint(0, 7)])
  
#Question 5: Creating and using a custom module
import math_operations as op

#Simple calculator
print("Simple Calculator")
calc = True
while calc == True:
  num1 = float(input("Enter number: "))
  operation = input("Enter operation, + for addition, - for subtraction, * for multiplication, or / for division: ")
  num2 = float(input("Enter number: "))
  
  if operation == "+":
    result = op.add(num1, num2)
    print(result)
  elif operation == "-":
    result = op.subtract(num1, num2)
    print(result)
  elif operation == "*":
    result = op.multiply(num1, num2)
    print(result)
  elif operation == "/":
    result = op.divide(num1, num2)
    print(result)
    
  if input("Enter True to continue or False to stop: ") == True:
    calc = True
  else:
    calc = False