try:
    num1,num2 = eval(input("enter two numbers,separate by comma"))
    result = num1/num2
    print(result)
except ValueError :
    print("zero is not allowed")
except SyntaxError:
    print("enter a number ")
except:
    print("some error occured")
finally:
    print("I will execute no matter what")