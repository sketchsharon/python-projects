d1={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,0:0}
d2={1:1,3:3,4:4,6:6,8:8,9:9}
c=[]
for value in list(d1.keys()):
    if value in list(d2.keys()):
        c.append(value)
print("The common keys are ",c)
