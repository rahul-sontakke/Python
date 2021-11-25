#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
len_letters = int(input("How many letters would you like in your password?\n")) 
len_symbols = int(input(f"How many symbols would you like?\n"))
len_numbers = int(input(f"How many numbers would you like?\n"))
password=''
total = len_letters + len_numbers + len_symbols

no_letters = len(letters)
no_symbols = len(symbols)
no_numbers = len(numbers)

letter=len_letters
number=len_numbers
symbol=len_symbols

final_index = 0

for i in range(0,total):

  final_index = 0

  while final_index == 0:
    random_char_index = random.randint(1,3)
    if random_char_index == 1:
      if letter != 0:
        final_index = 1
        letter -= 1  
      else: 
       continue 
    if random_char_index == 2:
      if number != 0:
        final_index = 2
        number -= 1
      else:
        continue
    if random_char_index == 3:
      if symbol != 0:
        final_index = 3       
        symbol -= 1
      else:
        continue  
  
  print(final_index)  
  
  if final_index == 1:
    random_letter_index = random.randint(0,no_letters-1)
    password += letters[random_letter_index]
  elif final_index == 2:
    random_number_index = random.randint(0,no_numbers-1)
    password += numbers[random_number_index]
  else: 
    random_symbol_index = random.randint(0,no_symbols-1)   
    password += symbols[random_symbol_index]

print(f"Your password is : {password}")

