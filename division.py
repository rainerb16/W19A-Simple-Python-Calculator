def divideNumbers(userNumOne, userNumTwo):
  try:
    answer = userNumOne / userNumTwo
  except ZeroDivisionError:
    print("Cannot divide by zero")
  else:
    print("Your result: " + str(answer))