print("Give me a number:")
num = input()
if num.isnumeric() :
    print("This number is an integer.")
else :
    try :
        floatNum = float(num)
        print("This number is a decimal.")
    except ValueError:
        print("error 555")      
        
