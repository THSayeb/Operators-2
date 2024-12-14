w = float(input("Enter your weight in kg "))
h = float(input("Enter your height in meter "))

BMI = w / h**2
print("Your BMI is ", BMI)

if BMI <= 18.4:
    print("You are under weight")
elif BMI <= 24.9:
    print("You are healthy")
elif BMI <= 29.9:
    print("You are over weight")
elif BMI <= 39.9:
    print("You are obese")
else:
    print("You are dead")