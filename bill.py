stock={'book':5,'pen':12,'pencil':8,'eraser':9}
price={'book':30,'pen':10,'pencil':5,'eraser':3}
cart={}
while True:
    print(stock)
    print(price)
    commodity=input("What do you need?: ")
    quantity=int(input("Mention the quantity: "))
    if stock[commodity]<quantity:
        print("The quantity required is more than available")
    else:
        cart[commodity]=quantity*price[commodity]
        if stock[commodity]-quantity<=0:
            stock[commodity]=0
        else:
            stock[commodity]-=quantity
    next=input("Do you need any other thing?(y/n): ")
    if next.lower()!='y':
        break
total=0
for value in cart.values():
    total=total+ value
print("Total amount : ",total)
