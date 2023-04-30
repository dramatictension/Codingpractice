
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


name1low = name1.lower()
name2low = name2.lower()

combinedname = name1low + name2low

t = combinedname.count("t")
r = combinedname.count("r")
u = combinedname.count("u")
e = combinedname.count("e")
l = combinedname.count("l")
o = combinedname.count("o")
v = combinedname.count("v")

true = t + r + u + e
love = l + o + v + e

finalscore = str(true) + str(love)

finalint = int(finalscore)

if finalint <=10 or finalint >=90:
    print(f"your Score is {finalint}, you go together like coke and mentos.")
elif finalint >=40 and finalint <=50:
    print(f"Your score is {finalint}, you are alright together.")
else:
    print(f"Your score is {finalint}.")
