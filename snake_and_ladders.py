from PIL import Image
from random import randint
end=100
def show_board():
    img=Image.open('board.jpg')
    img.show()
    
def check_ladder(pos):
    if pos==1:
        print('Ladder from 1 to 38')
        return 38
    elif pos==4:
        print('Ladder from 4 to 14')
        return 14
    elif pos==8:
        print('Ladder from 8 to 30')
        return 30
    elif pos==21:
        print('Ladder from 21 to 42')
        return 42
    elif pos==28:
        print('Ladder from 28 to 76')
        return 76
    elif pos==50:
        print('Ladder from 50 to 67')
        return 67
    elif pos==71:
        print('Ladder from 71 to 92')
        return 92
    elif pos==88:
        print('Ladder from 88 to 99')
        return 99
    else:
        #No ladder is encountered
        return pos
def check_snake(pos):
    if pos==32:
        print('Snake from 32 to 10')
        return 10
    elif pos==36:
        print('Snake from 36 to 6')
        return 6
    elif pos==48:
        print('Snake from 48 to 26')
        return 26
    elif pos==62:
        print('Snake from 62 to 18')
        return 18
    elif pos==88:
        print('Snake from 88 to 24')
        return 24
    elif pos==95:
        print('Snake from 95 to 56')
        return 56
    elif pos==97:
        print('Snake from 97 to 78')
        return 78
    else:
        #No snake encountered
        return pos
        
def play():
    while(1):
        no_comp=0
        no_human=int(input('No of Players:'))
        if(no_human>4):
            print("This game can't be played by more than 4 players:(")
            continue
        if(no_human!=4):
            no_comp=int(input('No of computers: '))
        if(no_human==1 and no_comp==0):
            print('You need one more player or a computer to play the game :(')
        elif (no_human + no_comp > 4):
            print("This game can't be played by more than 4 players:(")
        elif(no_human==0 and no_comp>0):
            print("This game can't be played by only computers")
        elif ((no_human + no_comp)<=4 and (no_human + no_comp)>1 and no_human>=1):
            break
    
    if(no_human==1):
        p1_name=input('Player 1, Please input your name: ')
        p1_pos=0
        if(no_comp==1):
            p2_name='computer'
            p2_pos=0
        if(no_comp==2):
            p2_name='computer 1'
            p2_pos=0
            p3_name='computer 2'
            p3_pos=0
        if(no_comp==3):
            p2_name='computer 1'
            p2_pos=0
            p3_name='computer 2'
            p3_pos=0
            p4_name='computer 3'
            p4_pos=0
    
    elif(no_human==2):
        p1_name=input('Player 1, Please input your name: ')
        p2_name=input('Player 2, Please input your name: ')
        p1_pos=0
        p2_pos=0
        if(no_comp==1):
            p3_name='computer'
            p3_pos=0
        if(no_comp==2):
            p3_name='computer 1'
            p3_pos=0
            p4_name='computer 2'
            p4_pos=0
    
    elif(no_human==3):
        p1_name=input('Player 1, Please input your name: ')
        p2_name=input('Player 2, Please input your name: ')
        p3_name=input('Player 3, Please input your name: ')
        p1_pos=0
        p2_pos=0
        p3_pos=0
        if(no_comp==1):
            p4_name='computer'
            p4_pos=0
    
    elif(no_human==4):
        p1_name=input('Player 1, Please input your name: ')
        p2_name=input('Player 2, Please input your name: ')
        p3_name=input('Player 3, Please input your name: ')
        p4_name=input('Player 4, Please input your name: ')
        p1_pos=0
        p2_pos=0
        p3_pos=0
        p4_pos=0
    
    turn=0
    #game driver for 2 players
    if((no_human+no_comp)==2):
        while(1):
            if turn%2 == 0:
                print(p1_name, ' your turn')
                print('Dice rolling!!') 
                dice = randint(1, 6)
                print('Dice showed: ',dice)
                p1_pos = p1_pos + dice
                p1_pos=check_ladder(p1_pos)
                p1_pos=check_snake(p1_pos)
                if(p1_pos>end):
                    print('Roll the dice such that you land on 100, try in next turn')
                    p1_pos=p1_pos-dice
                print(p1_name, "You are at position:", p1_pos)
                if(p1_pos==end):
                    print(p1_name, "Congratulations! You Won")
                    break
            else:
                print(p2_name, ' your turn')
                print('Dice rolling!!') 
                dice = randint(1, 6)
                print('Dice showed: ',dice)
                p2_pos = p2_pos + dice
                p2_pos=check_ladder(p2_pos)
                p2_pos=check_snake(p2_pos)
                if(p2_pos>end):
                    print('Roll the dice such that you land on 100, try in next turn')
                    p2_pos=p2_pos-dice
                print(p2_name, "You are at position:", p2_pos)
                if(p2_pos==end):
                    print(p2_name, "Congratulations! You Won")
                    break
            c=int(input("Any player, press 1 to continue or 0 to quit without a winner: "))
            if c==0:
                c_f=int(input("Are you sure (Yes(0), No(1)):"))
                if(c_f==0):
                    break
            turn=turn+1
            
    #game driver for 3 players        
    elif((no_human+no_comp)==3):
        while(1):
            if turn%3 == 0:
                print(p1_name, ' your turn')
                print('Dice rolling!!') 
                dice = randint(1, 6)
                print('Dice showed: ',dice)
                p1_pos = p1_pos + dice
                p1_pos=check_ladder(p1_pos)
                p1_pos=check_snake(p1_pos)
                if(p1_pos>end):
                    print('Roll the dice such that you land on 100, try in next turn')
                    p1_pos=p1_pos-dice
                print(p1_name, "You are at position:", p1_pos)
                if(p1_pos==end):
                    print(p1_name, "Congratulations! You Won")
                    break
            elif turn%3 == 1:
                print(p2_name, ' your turn')
                print('Dice rolling!!') 
                dice = randint(1, 6)
                print('Dice showed: ',dice)
                p2_pos = p2_pos + dice
                p2_pos=check_ladder(p2_pos)
                p2_pos=check_snake(p2_pos)
                if(p2_pos>end):
                    print('Roll the dice such that you land on 100, try in next turn')
                    p2_pos=p2_pos-dice
                print(p2_name, "You are at position:", p2_pos)
                if(p2_pos==end):
                    print(p2_name, "Congratulations! You Won")
                    break
            elif turn%3 == 2:
                print(p3_name, ' your turn')
                print('Dice rolling!!') 
                dice = randint(1, 6)
                print('Dice showed: ',dice)
                p3_pos = p3_pos + dice
                p3_pos=check_ladder(p3_pos)
                p3_pos=check_snake(p3_pos)
                if(p3_pos>end):
                    print('Roll the dice such that you land on 100, try in next turn')
                    p3_pos=p3_pos-dice
                print(p3_name, "You are at position:", p3_pos)
                if(p3_pos==end):
                    print(p3_name, "Congratulations! You Won")
                    break
            c=int(input("Any player, press 1 to continue or 0 to quit without a winner: "))
            if c==0:
                c_f=int(input("Are you sure (Yes(0), No(1)):"))
                if(c_f==0):
                    break
            turn=turn+1
    #game driver for 4 players
    elif((no_human+no_comp)==4):
        while(1):
            if turn%4 == 0:
                print(p1_name, ' your turn')
                print('Dice rolling!!') 
                dice = randint(1, 6)
                print('Dice showed: ',dice)
                p1_pos = p1_pos + dice
                p1_pos=check_ladder(p1_pos)
                p1_pos=check_snake(p1_pos)
                if(p1_pos>end):
                    print('Roll the dice such that you land on 100, try in next turn')
                    p1_pos=p1_pos-dice
                print(p1_name, "You are at position:", p1_pos)
                if(p1_pos==end):
                    print(p1_name, "Congratulations! You Won")
                    break
            elif turn%4 == 1:
                print(p2_name, ' your turn')
                print('Dice rolling!!') 
                dice = randint(1, 6)
                print('Dice showed: ',dice)
                p2_pos = p2_pos + dice
                p2_pos=check_ladder(p2_pos)
                p2_pos=check_snake(p2_pos)
                if(p2_pos>end):
                    print('Roll the dice such that you land on 100, try in next turn')
                    p2_pos=p2_pos-dice
                print(p2_name, "You are at position:", p2_pos)
                if(p2_pos==end):
                    print(p2_name, "Congratulations! You Won")
                    break
            elif turn%4 == 2:
                print(p3_name, ' your turn')
                print('Dice rolling!!') 
                dice = randint(1, 6)
                print('Dice showed: ',dice)
                p3_pos = p3_pos + dice
                p3_pos=check_ladder(p3_pos)
                p3_pos=check_snake(p3_pos)
                if(p3_pos>end):
                    print('Roll the dice such that you land on 100, try in next turn')
                    p3_pos=p3_pos-dice
                print(p3_name, "You are at position:", p3_pos)
                if(p3_pos==end):
                    print(p3_name, "Congratulations! You Won")
                    break
            elif turn%4 == 3:
                print(p4_name, ' your turn')
                print('Dice rolling!!') 
                dice = randint(1, 6)
                print('Dice showed: ',dice)
                p4_pos = p4_pos + dice
                p4_pos=check_ladder(p4_pos)
                p4_pos=check_snake(p4_pos)
                if(p4_pos>end):
                    print('Roll the dice such that you land on 100, try in next turn')
                    p4_pos=p4_pos-dice
                print(p4_name, "You are at position:", p4_pos)
                if(p4_pos==end):
                    print(p4_name, "Congratulations! You Won")
                    break
            c=int(input("Any player, press 1 to continue or 0 to quit without a winner: "))
            if c==0:
                c_f=int(input("Are you sure (Yes(0), No(1)):"))
                if(c_f==0):
                    break
            turn=turn+1
        
show_board()
play()