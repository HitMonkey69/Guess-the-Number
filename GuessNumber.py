#Guess the number game by HitMonkey69


import random
import pyfiglet

banner = pyfiglet.figlet_format('Guess the Number')
print(banner)
print('Choose between 0-100')

computer = random.randint(0,100)

while True:
    usr = int(input('Enter your number here:'))
    
    if usr > computer:
        if usr - computer < 10:
            print('You are 0-10 more')
        elif usr - computer < 20:
            print('You are 0-20 more')
        else:
            print('Your choice is greater than computers')

    if usr < computer:
        if computer - usr < 10:
            print('You are 0-10 less')
        elif computer - usr < 20:
            print('You 0-20 less')
        else:
            print('Your choice is lesser than computers')
        

    elif usr == computer:
        print('Voila!')
        print('Press 1 to play again or press 0 to quit')
        usr = int(input('Enter your choice here:'))
        if usr == 1:
            print('Here we go again...')
            computer = random.randint(0,100)

        elif usr == 0:
            print('Thanks for playing')
            break

        else:
            banner = pyfiglet.figlet_format('Crashing...')
            print(banner)
            break
    
        