'''
Created on 23-Mar-2019

@author: sourav nandi
'''
try:
    n=int(input())
    l=[]
    for i in range(n):
        l.append(input())
    minl=100000
    for i in range(len(l)):
        if len(l[i])<minl:
            minl=len(l[i])
    count=[]
    for j in range(n):
        count.append(0)
    for j in range(n-1):
        m=[0]
        for i in range(minl):
            if(m[0]==i):                    #for continious match of string
                if l[j][i]==l[j+1][i]:
                    count[j]=count[j]+1
                    m[0]=i+1
    m=""
    for i in range(max(count)):
        m=m+l[1][i]
    print(m)
except:
    print("") 
        
    
    
