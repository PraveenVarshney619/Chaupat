def grid():   
    for i in range(41):
        if i%8==0:
            print(" #"*65)
        else:
            print("#","#","#","#","#","#",sep=" "*25)
