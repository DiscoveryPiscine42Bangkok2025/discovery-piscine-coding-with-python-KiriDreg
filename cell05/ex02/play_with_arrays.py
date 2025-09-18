array = [2, 8, 9, 48, 8, 22, -12, 2]
print(f"Original array: {array}")
result = []
for i in array :
   temp = i + 2
   if temp > 5 :
    result.append(temp)

print(f"New array: {result}")