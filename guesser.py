'''
guesses a number between 1 and 100
'''
import random



def main():
    print("Guess a number between 1 and 100")
    #randomNumber = 35         #testing purposes
    randomNumber = random.randint(1,100)
    found = True

    while found:
        userguess = int(input('Your guess: '))
        if userguess == randomNumber:
            print("Correct!")
            again = input('press "y" to play again: ')
            if again == 'y':
                found = True
            else:
                found = False
        elif userguess > randomNumber:
            print('Lower')
        else:
            print('Higher')

if __name__ == '__main__':
    main()