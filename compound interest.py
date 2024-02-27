p=float(input("Enter the investment amount: "))
t=int(input("Enter the number of years: "))
r=int(input("Enter the rate of interest per annum: "))
print("Year\tStarting Balance\tInterest\tEnding Balance")
sb=p
for i in range(1,t+1):
    interest=(sb*r)/100
    eb=sb+interest
    print(i,"\t",'%.2f'%sb,"\t\t",'%.2f'%interest,"\t",'%.2f'%eb)
    sb=eb
print("Ending balance: $",'%.2f'%eb)
print("Total interest earned: $",'%.2f'%(eb-p))
