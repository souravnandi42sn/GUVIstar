'''
Created on 20-Mar-2019

@author: sourav nandi
'''
try:
    n=input()
    m=int(n[0])**3+int(n[1])**3+int(n[2])**3
    if(m==int(n)):
        print("yes")
    else:
        print("no")
except:
    print("no")
