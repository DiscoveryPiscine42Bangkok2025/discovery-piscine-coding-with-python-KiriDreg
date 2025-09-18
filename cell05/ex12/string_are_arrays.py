import sys
import re
if len(sys.argv) == 1 :
    print("none")
else : 
        Zarr = ''.join(re.findall("z"," ".join(sys.argv[1:])))
        print(Zarr)
        









            