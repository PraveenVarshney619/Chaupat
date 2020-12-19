import random 
import time
def toss():
    t=(random.randint(0,1) for i in range(4))
    return t
def steps():
    tup=(toss())
    s=0
    for i in tup:
        s+=i
    return s
def pawn():
    goti=[]
    for i in toss():
        if i==1:
            goti.append(">")
        else:
            goti.append("^")
    if goti==[">",">",">",">"] or goti==["^","^","^","^"]:
        pawn()
    else:
        return goti
def color():
    colors=["red","green","blue","yellow"]
    col={"red":["R1","R2","R3","R4"],
         "green":["G1","G2","G3","G4"],
         "blue":["B1","B2","B3","B4"],
         "yellow":["Y1","Y2","Y3","Y4"]}
    return random.choice(colors)
import board
def disp_grid():
    return board.grid()
def play():
    print("LET'S PLAY CHAUPAT !!!")
    n=int(input("Enter \n1 - Play with humans\n2 - Play with computer\n0 - Exit   :\n"))
    player_data={}
    if n==1:
        p=int(input("How many players are going to play? : "))
        for i in range(p):
            if p>4 or p<=1:
                print("Not allowed...")
                time.sleep(2)
                play()
                break
            name=input(f"Enter player {i+1} name : ")
            player_data[f"P{i+1}"]=[name,color()]
        print("Starting game !")
        time.sleep(2)
        disp_grid()
    elif n==2:
        name=input("Enter player's name: ")
        player_data[name]=[]
        print("Starting game !")
        time.sleep(2)
        disp_grid()
    elif n==0:
        print("Thanks for playing !!!")
        for i in range(3):
            time.sleep(1)
            print(3-i,"...")
        quit()
    else:
        print("Enter correct choice!")
        play()

play()





 

