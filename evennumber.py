'''
Created on 20-Mar-2019

@author: sourav nandi
'''
def isprime(n,m):
    l=[]
    for i in range(n+1,m):
        if(i%2==0):
            l.append(i)
    return(l)
try:
    n=input().split(" ")
    l=isprime(int(n[0]),int(n[1]))
    print(" ".join(str(x) for x in l))
except:
    print("")
