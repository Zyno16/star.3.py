l = int(input("enter the number"))
for i in range(1,l+1):
    for j in range(1,l-i+1):
        print("  ",end ="")
    for j  in range (1,(2*i+1-1)):
        if j == 1 or j == 2*i-1 or i ==l:
            print("* ",end ="")
        else:
            print("  ",end ="")

    print()
                 
    


    