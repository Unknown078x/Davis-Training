# BMI calculation

w = float(input("Weight (kg): "))
h = float(input("Height (m): "))

bmi = w / (h*h)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
else:
    print("Overweight")