#Question 1
name = input("What is your name? ")
age = input("How old are you? ")
print("Greetings, " + name + ", " + age + " years old.")

#Question 2
rect_length = int(input("Enter length of rectangle: "))
rect_width = int(input("Enter width of rectangle: "))
print(rect_length * rect_width)

#Question 3
celsius = float(input("Enter temperature in Celsius: "))
print(celsius)
fahrenheit = (celsius * 9 / 5) + 32
print(f"{fahrenheit:.2f}")