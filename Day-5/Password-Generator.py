import random
print("Welcome to the password generator 😃")
input("Press Enter to continue\n")
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','&','-','_']
letter=int(input("Enter the number of letters you want in your password\n"))
special=int(input("Enter the number of special symbols you want in your password\n"))
number=int(input("Enter the number of digits you want in your password\n"))
total=letter+special+number
password=[]
for i in range (1,letter+1):
  password.append(random.choice(letters))
for i in range (1,number+1):
  password.append(random.choice(numbers))
for i in range (1,special+1):
  password.append(random.choice(symbols))

random.shuffle(password)

fpassword= ""
for char in password:
  fpassword+=char
print(f"Your password is {fpassword}")
