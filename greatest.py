try:
    n=input().split(" ")
    if(int(n[0])>int(n[1])):
        if(int(n[0])>int(n[2])):
            print(int(n[0]))
        else:
            print(int(n[2]))
    elif(int(n[1])>int(n[2])):
        print(int(n[1]))
    else:
        print(int(n[2]))
except:
    print("invalid")
