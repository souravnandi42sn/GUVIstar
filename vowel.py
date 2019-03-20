try:
    n=input()
    if ((n>='a' and n<= 'z') or (n>='A' and n<='Z')):
        if(len(n)==1):
            if n is ["a","e","i","o","U"] or ["A","E","I","O","U"]:
                print("Vowel")
            else:
                print("constant")
        else:
            print("invalid")
    else:
        print("invalid")
except :
    print("invalid")
