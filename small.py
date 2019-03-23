'''
Created on 23-Mar-2019

@author: sourav nandi
'''
try:
    n=input().split(" ")
    if int(n[1])>0:
        min=int(n[0])
        m=n[0]
        l=[]
        for i in range(len(n[0])):
            for h in range(1,len(n[0])+1):
                j=m[i:h]
                if(j!="" and len(j)==len(n[0])-int(n[1])):
                    if(int(j)<min):
                        l.append(m[i:h])
        mi=int(n[0])
        for i in range(len(l)):
            if int(l[i])<mi:
                mi=int(l[i])
        print(mi)
    else:
        print(int(n[0]))
except:
    print(int(n[0])) 
    

        
