#Question 1
x = 6
x += 3
y = 2
y *= 2
result = x / y
print(result)

#Question 2
a,b,c = 20,38,83

if a > b:
  pass
elif b % 2 == 0:
  pass
elif c <= a:
  pass

if a > b or b % 2 == 0 and c <= a:
  final_condition = True
  
#Question 3
score = int(input("Input test score (0-100): "))

if score >= 90 and score <= 100:
  print("A")
elif score >= 80 and score <= 89:
  print("B")
elif score >= 70 and score <= 79:
  print("C")
elif score >= 60 and score <= 69:
  print("D")
else:
  print("F")
  
#Question 4
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

operation = input("Enter operation, + for addition, - for subtraction, * for multiplication, and / for division: ")

if num2 == 0:
  print("Error, cannot divide by zero.")
else:
  if operation == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
  if operation == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
  if operation == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
  if operation == "/":
    print(f"{num1} / {num2} = {num1 / num2:.2f}")
