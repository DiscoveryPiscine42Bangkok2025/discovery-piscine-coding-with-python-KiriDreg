print("Enter the first number:")
firstNum = int(input())
print("Enter the second number:")
SecondNum = int(input())
multi = firstNum * SecondNum 
print(str(firstNum) + " x " + str(SecondNum) + " = " + str(multi) )
if multi < 0 : print("The result is negative.")
elif multi > 0 : print("This number is positive.")
else : print("This number is both positive and negative.")