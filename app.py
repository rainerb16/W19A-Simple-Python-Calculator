import addition
import subtraction
import multiplication
import division

print("Welcome to SimpleCalc! \n\nPlease select an operation: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

userChoice = input()
userNumOne = int(input("First Number: "))
userNumTwo = int(input("Second Number: "))

if userChoice == "1":
  addition.addNumbers(userNumOne, userNumTwo)
elif userChoice == "2":
  subtraction.subtractNumbers(userNumOne, userNumTwo)
elif userChoice == "3":
  multiplication.multiplyNumbers(userNumOne, userNumTwo)
elif userChoice == "4":
  division.divideNumbers(userNumOne, userNumTwo)
else:
  print("There was an error, please choose 1, 2, 3, or 4")
