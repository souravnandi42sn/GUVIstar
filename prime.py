'''
Created on 20-Mar-2019

@author: sourav nandi
'''
def factors(n):
    l=[]
    for i in range(1,n+1):
        if(n%i==0):
            l.append(i)
    return l
    
try:
    n=input()
    if(int(n)<=1000):
        l=factors(int(n))
        if(l==[1,int(n)]):
            print("yes")
        else:
            print("no")  
    else:
        print("no")    
except:
    print("no")
