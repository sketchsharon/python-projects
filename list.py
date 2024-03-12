k=int(input("Enter the number which should be considered to create the second list: "))
n=int(input("Enter the no of elements: "))
l,m=[],[]
for i in range(n):
    j=int(input("Enter the element: "))
    l.append(j)
    if l[i]<k:
        m.append(l[i])
print("The new list is ",m)
