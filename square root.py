import math
x=int(input("Enter a positive value: "))
y=math.sqrt(x)
z=1
for i in range(1,x//2):
    z=(z+x/z)/2
    if z==y:
        break
print("square root of ",x,"is ",'%8.8f'%z)
