try:
    n=input()
    if(n>="a" and n<="z") or (n>="A" and n<="Z"):
        print("")
    else:
        print(len(n))
except:
    print("")
