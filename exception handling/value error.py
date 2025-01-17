try:
  number = int(input("enter a number"))
  print("The number entered is",number)
except ValueError as ex:
  print("exception is ",ex)

print("outside try block")