# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
heightn = float(height)
weightn = int(weight)

result = weightn / heightn ** 2

resultin = int(result)
print (resultin)
if resultin < 18.5:
  print(f"Your BMI is {resultin},  you are underweight.")
elif resultin < 25:
   print(f"Your BMI is {resultin},  you have a normal weight.")
elif resultin < 28:
   print(f"Your BMI is {resultin},  you are slightly overweight.")
elif resultin < 35:
   print(f"Your BMI is {resultin},  you are obese.")  
else:
  print(f"Your BMI is {resultin},  you are clinically obese.") 



