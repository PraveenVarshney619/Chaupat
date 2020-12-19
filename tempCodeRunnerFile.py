for i in range(41):
        for j in range(65):
            if i%8==0:
                if j==64:
                    print(" #",end="\n"*7)
                else:
                    print(" #",end="")
            elif j%8==0 and i%8!=0:
                print("#",end=" ")