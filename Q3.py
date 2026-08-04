print("using logic:")
data=[10,12,15,18,20,20,22,25]
fre={}
for i in data:
    if i in fre:
        fre[i]+=1
    else:
        fre[i]=1
mode=max(fre,key=fre.get)
print("max observation",mode)
print("using library function:")
from statistics import mode
print(mode(data))

