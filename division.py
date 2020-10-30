def divideNumbers(userNumOne, userNumTwo):
  try:
    answer = userNumOne / userNumTwo
  except ZeroDivisionError:
    print("Cannot divide by zero")
  print("Your result: " + str(answer))