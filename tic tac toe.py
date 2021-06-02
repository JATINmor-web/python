import random
import time
combinations = [
    [1,2,3],[4,5,6],[7,8,9],
    [1,4,7],[2,5,8],[3,6,9],
    [1,5,9],[3,5,7]
    ]
positions = [i for i in range(1,10)]
positions_occupied =[]
def gameBoard():
    print(
        f"""
                {positions[0]}  |  {positions[1]}  |  {positions[2]}
                ----------------
                {positions[3]}  |  {positions[4]}  |  {positions[5]}
                ----------------
                {positions[6]}  |  {positions[7]}  |  {positions[8]}
                
        """
        )

def userMove(choice):
    pos = int(input("Enter Your Position"))
    positions[pos-1]=choice
    gameBoard()
    positions_occupied.append(pos)
    msg = checkWinner(pos,choice)
    return msg

def cpu_move(cpu_ch):
    cpu_pos = random.randint(1,9)
    print(f"cpu positions : {cpu_pos}")
    if cpu_pos in positions_occupied:
        cpu_move(cpu_ch)#recursive function
    else:
        positions[cpu_pos-1]=cpu_ch
        gameBoard()
        positions_occupied.append(cpu_pos)
        msg = checkWinner(cpu_pos,cpu_ch)
        return msg

def checkWinner(pos,choice):
    for i in range(len(combinations)):
        if pos in combinations[i]:
            index = combinations[i].index(pos)
            combinations[i][index]=choice

    for i in range(len(combinations)):
        if combinations[i][0] == choice and combinations[i][1] == choice and combinations[i][2] == choice:
           return "winner" 
            

gameBoard()
ch = input("Enter your Choice : X | 0 ->")
if ch=='X':
    cpu_ch=0
else:
    cpu_ch='X'
Game=True
while Game:
    '''
    print("combinations:",combinations)
    print("occupied :",positions_occupied)
    print("positions :",positions)
    '''
    msg=userMove(ch)
    if msg=="winner":
        print("User Wins")
        break
    print("CPU TURN.....")
    time.sleep(5)
    msg = cpu_move(cpu_ch)
    print(msg)
    if msg=="winner":
        print("CPU Wins")
        break
