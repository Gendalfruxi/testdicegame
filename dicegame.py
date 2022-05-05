
import random
currentroller = 0
maxpoint = 40

def starting_dice():
    start = random.randrange(0,1)
    if start == 0:
        return 1
        print('1st player srarts')
    else:
        return 2
        print('2nd player starts')


class Dice:
    def roll(self):
        one = random.randrange(1,7)
        two = random.randrange(1,7)
        return one,two

player1=Dice()
player2=Dice()

#print(player1.roll())
#print(player1.roll(), sum(player1.roll()))

player1_totalscore=0
player2_totalscore=0

player1_currentscore=0
player2_currentscore=0

def dice1(a):
    global player1_currentscore,player1_totalscore,currentroller
    #player1_totalscore=0
    if a.lower() == 'r':
        currentroll = player1.roll()
        print(currentroll)
        if currentroll[0]!=currentroll[1]:
            player1_currentscore += sum(currentroll)
            print('player 1 your total score is', player1_currentscore)
        else:
            print('zero bankrupt your current score is nulled, next move goes to player 2')
            player1_currentscore = 0
            currentroller = 2
    elif a == 'hold':
        player1_totalscore = player1_currentscore
        currentroller = 2
        print('player 1 your roll is over, your current total score is ',player1_totalscore )
    else:
        print('please enter proper command')


def dice2(a):
    global player2_currentscore,player2_totalscore,currentroller
    #player1_totalscore=0
    if a.lower() == 'r':
        currentroll = player2.roll()
        print(currentroll)
        if currentroll[0]!=currentroll[1]:
            player2_currentscore += sum(currentroll)
            print('player 2 your total score is', player2_currentscore)
        else:
            print('bankrupt your current score is nulled, next move goes to player 1')
            player2_currentscore = 0
            currentroller = 1
    elif a == 'hold':
        player2_totalscore = player2_currentscore
        currentroller = 1
        print('player 2 your roll is over, your current total score is ',player2_totalscore )
    else:
        print('please enter proper command')



print("hi, for rules and commands type help")
while True:
    c = input(' >> ')
    if c == 'start':
        currentroller = starting_dice()
        print(currentroller)
        if currentroller == 1:
            print('1st player srarts please type r to roll your dice')
        else:
            print('2nd player srarts please type r to roll your dice')
    elif c == 'res':
        if player1_totalscore>player2_totalscore:
            print('1st player wins')
        elif player1_totalscore==player2_totalscore:
            print('draw')
        else:
            print('2nd player wins')
        break
    elif c == 'help':
        print('commands: \n help - show all commands \n start - starting the game \n r - roll a dice \n hold - current score is saved and next players time to play \n "two of the same" is unlucky roll and all your score is nulled ')
    elif currentroller ==1:
        dice1(c)
    elif currentroller ==2:
        dice2(c)
    else:
        print('please enter propper command')
    if player1_totalscore == maxpoint:
        print('player 1 wins')
        break
    elif player1_totalscore>maxpoint or player1_currentscore>maxpoint:
        print('burnout, player 2 wins')
        break
    if player2_totalscore == maxpoint:
        print('player 2 wins')
        break
    elif player2_totalscore>maxpoint or player2_currentscore>maxpoint:
        print('burnout, player 1 wins')
        break
    
