import sys
if len(sys.argv) == 1 : 
    print("none")
else :
    para = [i.upper() for i in sys.argv]
    print(para[1:])


