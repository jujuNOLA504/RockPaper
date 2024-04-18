import random

exit = False
user_points = 0
computer_points = 0

while exit == False:
    options = ['rock', 'paper', 'scissors']
    user_input = input('Choose rock, paper, scissors or exit:')
    computer_input = random.choice(options)

    if user_input == 'exit':
        print('Good Bye')
        print('You won a total score of '+str(user_points)+' and the computer total score is '+str(computer_points))
        exit = True

    if user_input == 'rock':
        if computer_input == 'rock':
            print('Your input is rock')
            print('My input is rock')
            print('It is a tie!')
        elif computer_input == 'paper':
            print('Your input is rock')
            print('My input is paper')
            print('AI wins!')
            computer_points += 1
        elif computer_input == 'scissors':
            print('Your input is rock')
            print('My input is scissors')
            print('You win!')
            user_points += 1

    elif user_input == 'paper':
        if computer_input == 'rock':
            print('Your input is paper')
            print('My input is rock')
            print('You win!')
            user_points += 1
        elif computer_input == 'paper':
            print('Your input is paper')
            print('My input is paper')
            print('It is tied up!')
        elif computer_input == 'scissors':
            print('Your input is paper')
            print('My input is scissors')
            print('AI wins!')
            computer_points += 1

    elif user_input == 'scissors':
        if computer_input == 'rock':
            print('Your input is scissors')
            print('My input is rock')
            print('AI wins!')
            computer_points += 1
        elif computer_input == 'paper':
            print('Your input is scissors')
            print('My input is paper')
            print('You Win!')
            user_points += 1
        elif computer_input == 'scissors':
            print('Your input is scissors')
            print('My input is scissors')
            print('It is tied up!')


    elif user_input != 'rock' or user_input != 'paper' or user_input != 'scissors':
            print('Invalid input')