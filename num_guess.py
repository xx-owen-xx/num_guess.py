# Owen Fissel
# ENG 103
#num_guess.py


# prompt user for integer to be guessed
goal = int(input('Enter the integer for the player to guess. '))

# guess counter

guess_count = 0

#prompt user for first guess

guess = int(input('Enter your guess.\n'))
guess_count += 1

#loop untill goal

while guess!= goal:
    if guess > goal:
        guess = int(input('Too high - try again:\n'))
    else:
        guess = int(input('Too low - try again:\n'))
    guess_count += 1
    
#print results
if guess_count == 1:
    print('You guessed it in 1 try.')
else:
    print(f'You guessed it in {guess_count} tries.')
    

        
