'''
Created on 20-Mar-2019

@author: sourav nandi
'''
try:
    n=input()
    m=n[::-1]
    if(len(n)<=1000):
        if(m==n):
            print("yes")
        else:
            print("no")
    else:
        print("no")    
except:
    print("no")
