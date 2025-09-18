import sys
import re
if len(sys.argv) == 1:
    print("none")
else : 
    for i in sys.argv[1:] :
        if re.findall("ism",i) :
            continue
        print(i + "ism")