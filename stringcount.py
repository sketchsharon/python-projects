a="India is a sovereign socialist secular democratic republic India is a nice country"
b=a.split()
e={}
for i in range(0,len(b)):
    if b[i] in list(e.keys()):
        e[b[i]]+=1
    else:
        e[b[i]]=1
print("The frequency of each word in the given string is as follows:")
for i in e:
    print(i,":",e[i])
