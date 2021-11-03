print("Welcome to the love percentage calculator ❤️")
name=input("Enter your name\n")
partner=input("Enter your partner name\n")
name=name.lower()
partner=partner.lower()

#for word TRUE
t=name.count("t")+partner.count("t")
r=name.count("r")+partner.count("r")
u=name.count("u")+partner.count("u")
e=name.count("e")+partner.count("e")

#for word LOVE
l=name.count("l")+partner.count("l")
o=name.count("o")+partner.count("o")
v=name.count("v")+partner.count("v")

true=t+r+u+e
love=l+o+v+e

print(f"Your love percentage is {true}{love}% ")
