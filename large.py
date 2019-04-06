try:
    n=input()
    m=input()
    m=m[:int(n)]
    c=[int(m[i]) for i in range(int(n))]
    c.sort()
    c=c[::-1]
    b=[str(c[i]) for i in range(int(n))]
    b="".join(b)
    if(int(b)==0):
        b=str(0)
    print(b)
except:
    print("")
