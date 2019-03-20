
try:
    n=int(input())
    if n>=0:
        if n%2==0:
            print("Even")
        elif(n==0):
            print("Even")
        else:
            print("Odd")
    else:
        print("invalid")
except Exception as e:
    print(e)
    
