data=[10,12,15,18,20,20,22,25]
fre={}
for value in data:
    if value in fre:
        fre[value]+=1
    else:
        fre[value]=1
mode=max(fre,key=fre.get)
print("max observation",mode)

#OR

from statistics import mode
data=[10,12,15,18,20,20,22,25]
print(mode(data))

