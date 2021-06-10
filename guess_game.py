guess = None
value = 5
trial = 5

print("WELCOME TO OUR GUESS GAME")


while trial > 0:
    print('Your remaining trial is {}'.format(trial))
    guess = int(input('enter a number: '))
    if guess == value:
        print('You win')
        break
    
    else:
        trial = trial-1
else:
    print('You loss')
    