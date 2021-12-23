slist=list(map(int, input()))
slist.sort(reverse=True)

all=slist[0]

for i in range(1, len(slist)):
    if slist[i]==1:
        all+=1
    elif slist[i]!=0:
        all*=slist[i]
print(all)
