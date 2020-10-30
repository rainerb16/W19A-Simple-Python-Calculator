def divideNumbers(userNumOne, userNumTwo):
  try:
    answer = userNumOne / userNumTwo
    print("Your result: " + str(answer))
  except ZeroDivisionError:
    print("Cannot divide by zero")