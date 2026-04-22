#Question 1
def greet():
  print("Hello World!")
  
greet()

#Question 2
def personalized_greeting(name):
  print("Greetings, " + name)
  
personalized_greeting("Siphosethu Sage Dyan")

#Question 3
def square(num):
  return num ** 2

print(square(5))

#Question 4
def rectangle_area(length, width):
  return length * width

print(rectangle_area(4, 5))

#Question 5
def apply_operation(func, num):
  return func(num)

def double(num):
  return num * 2

print(apply_operation(double, 7))

print(apply_operation(square, 3))