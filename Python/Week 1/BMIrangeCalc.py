# This program asks the user for their height and weight, calculates BMI and assigns their BMI into ranges
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

#To not have more than 1 decimal after, bmi is being converted into a float with 1 decimal

bmi = weight / (height * height)
bmiInt = round(bmi , 1)
bmiFinal = round(bmiInt)

if bmiInt <18.5:
    print(f"Your BMI is {bmiFinal} are underweight.")
elif bmiInt >=18.5 and bmiInt <=25:
    print(f"Your BMI is {bmiFinal}, you have a normal weight.")    
elif bmiInt >25 and bmiInt <=30:
    print(f"Your BMI is {bmiFinal}, you are slightly overweight.")
elif bmiInt >30 and bmiInt <=35:
    print(f"Your BMI is {bmiFinal}, you are obese.")
elif bmiInt >35:
    print(f"Your BMI is {bmiFinal}, you are clinically obese.")
else:
    print("There was an error. Make sure to input valid numbers!")
