#BMI Calculator
w=int(input("Enter your weight(in kg)"))
h=float(input("Enter your height(in cm)"))
BMI= w/((h/100)**2)
print("Your BMI is ",BMI,end=" ")
print()
if BMI<18.5:
    print("underweight")
elif BMI<25:
    print("Normal")
elif BMI<30:
    print("Overweight")
else:
    print("You need to control asap")
