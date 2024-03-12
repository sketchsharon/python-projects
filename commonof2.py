l,m=[],[]
n=int(input("Enter the length of list l: "))
for i in range(n):
    j=int(input("Enter the elements: "))
    l.append(j)
o=int(input("Enter the length of list m: "))
for i in range(o):
    j=int(input("Enter the elements: "))
    m.append(j)
p=[]
for i in l:
    if i in m:
        p.append(i)
print("The elements common in both lists are ",p)
