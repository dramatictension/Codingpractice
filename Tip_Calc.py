#This program calculates your personal tip after doing some math.

dollarsspent = input("How much money did you spend? ")
tippercent = input("What percentage of tip do you want to give? ")
people = input("How many people are there? ")

#Instead of creating new vars for multiplicatives and fractions, this is doing the math in single lines. Code can be amended to
#Include additional vars for more easily understood math
basetip = float(dollarsspent) / 100 * int(tippercent)
persontip = round(basetip) / int(people)

print(f"Your personal tip is {persontip} dollars.")