#project9a
import math
a=int(input("input alphabets in ascii value 65-90:"))
b=math.pow(a,99)
b=int(b)
for i in range(65,b):
    print(chr(i),end=" ")
print(b)
