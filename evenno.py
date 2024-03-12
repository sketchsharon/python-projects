l,m=[],[]
n=int(input("Enter the length of list: "))
for i in range(n):
    a=int(input("Enter the elements of list: "))
    l.append(a)
    if a%2==0:
        m.append(a)
m.sort()
print("New list containing even numbers is ",m)
