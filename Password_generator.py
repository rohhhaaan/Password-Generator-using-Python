#Python program to generate password using random function
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator!")
nr_letters = int(input("How many letters should be there in the password?\n"))
nr_symbols = int(input(f"How many symbols should be there?\n"))
nr_numbers = int(input(f"How many numbers should be there?\n"))

#easy method
password = ""
 for char in range(0, nr_letters):
     password  += random.choice(letters)

for char in range(0, nr_symbols):
   password += random.choice(symbols)

for char in range(0, nr_numbers):
    password += random.choice(numbers)

 print(password)

#hard level
password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

 for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)