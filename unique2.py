try:
    n=input()
    m=input()
    m=m[:int(n)]
    c=[0 for i in range(int(n))]
    for i in range(len(m)):
        for j in range(i+1,int(n)):
            if(m[i]==m[j]):
                c[i]=c[i]+1
    b=[]
    
    for i in range(int(n)):
        if(int(c[i])>0):
            b.append(int(m[i]))
    b=list(set(b))
    b.sort()
    g=len(b)
    b=[str(b[i]) for i in range(g)]
    b="".join(b)
    print(b)
except:
    print("")
