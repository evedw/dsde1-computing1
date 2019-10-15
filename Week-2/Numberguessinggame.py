#This is my number guessing game, guess between 1-10
print('Hello and welcome to Eves number guessing game!')
print('What is your name?')
name = input()
print('Hi ' + name)
print('Lets play a game!')

#picking a number
print('Guess the number between 1 and 10 that i am thinking of')
import random
Computerguess = random.randint(1,10)
Userguess = input()
Userguess = int(Userguess)


print(Userguess==Computerguess)
if Userguess == Computerguess:
    import sys
    sys.exit()
if Userguess != Computerguess:
    print('Ohh unlucky thats incorrect ...')
print('Guess again?')
print('y/n')
import sys
Continue = input()
if Continue == 'y':
    print('Pick your new number')
    import random
if Continue == 'n':
    sys.exit()

Computerguess = random.randint(1,10)
Userguess = input()
Userguess = int(Userguess)





