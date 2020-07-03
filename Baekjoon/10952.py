addlist=[]

while True:
    a,b=input().split( )
    c=int(a)+int(b)
    
    if c==0:
        break;
    addlist.append(c);

for k in addlist:
    print(k)
