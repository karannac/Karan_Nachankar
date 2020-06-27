import random 
import time

def dice_roll():
    diceroll = random.randint(1, 6)

    return diceroll 

    
def simulater():
    a = 0
    b = 0
    player1 = 0
    player2 = 0
    player1wins = 0
    player2wins = 0
    rounds = 1
    a = input('Enter P1 Name: ')
    b = input('Enter P2 Name: ')

    while rounds != 6:
        print(' ')
        print('Round(s) = ', rounds)
        
        print(a, 'IS ROLLING THE DICE........')
        time.sleep(1)
        player1 = dice_roll()
        time.sleep(1)

        print(a + ' Dice Value = '+ str(player1))
        print(' ')
        print(b,'IS ROLLING THE DICE........')
        time.sleep(1)
      
        player2 = dice_roll()
        time.sleep(1)
        
        print(b + ' Dice Value= ' + str(player2))

        rounds = rounds + 1

        if player1 == player2:
          print('*')
          print("OOPPSS It'S A DRAW")
        elif player1 > player2:
          print('*')
          print(a, 'WINS !!!!!!!!!!!!!!!!')
          player1wins = player1wins + 1
        else:
          print('*')
          print(b, 'WINS !!!!!!!!!!!!!!!!')
          player2wins = player2wins + 1

    if player1wins == player2wins:
      print('$')
      print('$')
      print('THERE IS NO WINNER..ITS A DRAW')
    elif player1wins > player2wins:
      print('$')
      print('$')
      print('AND.....THE WINNER IS ' + a + ' HURRAY ***')
    else:
      print('$')
      print('$')
      print('AND.....THE WINNER IS ' + b + ' HURRAY ***')


simulater()
