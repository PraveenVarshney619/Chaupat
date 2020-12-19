def grid():   
    for i in range(41):
        for j in range(129):
            if i%8==0:
                if j==128:
                    print("#",end=" ")
                elif j==0:
                    print(" #",end="")
                else:
                    print("#",end="")
            elif i%8!=0:
                if j%25==0:
                    if j==128:
                        print("#",end="")
                    else:
                        print("#",end=" "*25) 
        print()  


'''
m1=[" #" for i in range(14)]
m2=["#" for i in range(7)]
for row in range()
'''