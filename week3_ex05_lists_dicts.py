#Question 1: Creating and Modifying Lists
fruits = ["kiwi", "mango", "pineapple", "granadilla", "grape"]

#Add a fruit at the end of the list
fruits.append("apple")

#Add a fruit at the start of the list
fruits.insert(0, "banana")

#Remove a fruit from the list
fruits.remove("grape")

#Print list
print(fruits)

#Question 2: List Operations
num_lst = [1, 2, 3, 4, 5]

#Making a new list from another list, a list of squared numbers
num_lst_sqr = [num ** 2 for num in num_lst]

sum = 0
#Finding the sum of numbers
for i in num_lst:
  sum += i

#Finding the average of numbers
average = sum / len(num_lst)

print(f"Sum: {sum}")
print(f"Average: {average}")

#Question 3: Creating and Modifying Dictionaries
countries = {"Algeria":"Algiers", "Egypt":"Cairo", "Ethiopia":"Addis Ababa", "Kenya":"Nairobi", "Nigeria":"Abuja", "Japan":"Tokyo"}

#Adding a new country-capital pair
countries["South Africa"] = "Cape Town"

#Update the capital of an existing country
countries["South Africa"] = "Pretoria"

#Remove a country-capital pair
countries.pop("Japan")

print(countries)

#Question 4: Dictionary Operations
fruit_colors = {"Apple":"Red", "Pear":"Green", "Banana":"Yellow", "Kiwi":"Brown", "Olive":"Green", "Blueberry":"Blue"}

#Print the keys only
print(fruit_colors.keys())

#Print the values only
print(fruit_colors.values())

#Print the items
print(fruit_colors.items())

#Check if a fruit is in the dictionary and print its color
fruit_search = input("Enter name of fruit: ")
if fruit_search in fruit_colors:
  print(fruit_colors[fruit_search])
else:
  print("There's no such fruit in your dictionary.")