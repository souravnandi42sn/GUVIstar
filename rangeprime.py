'''
Created on 20-Mar-2019

@author: sourav nandi
'''
def factors(n):
    l=[]
    for i in range(1,n+1):
        if(n%i==0):
            l.append(i)
    return(l)   
def isprime(n,m):
    g=[]
    for i in range(n+1,m):
        l=factors(i)
        if(l==[1,i]):
            g.append(i)
    return(g)
try:
    n=input().split(" ")
    l=isprime(int(n[0]),int(n[1]))
    print(" ".join(str(x) for x in l))
except:
    print("")
