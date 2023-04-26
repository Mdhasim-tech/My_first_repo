import time
import random

lst = ['stone', 'paper', 'scissor']
number_of_turns = 4
human_point = 0
comp_point = 0
for i in range(number_of_turns):

    comp_choice = random.choice(lst)
    human_choice = input('what do you choose--\n stone,paper or scissor?')

    if comp_choice == human_choice:
        print(f'you chose {human_choice} and the computer also chose {comp_choice}' + '\n this turn is nullified.')

        time.sleep(2)
    elif comp_choice == 'stone' and human_choice == 'scissor':
        print('you loose!!\n' + f'you chose {human_choice} and the computer chose {comp_choice}')
        comp_point += 1
        time.sleep(2)

    elif comp_choice == 'paper' and human_choice == 'stone':

        print('you loose!!\n' + f'you chose {human_choice} and the computer chose {comp_choice}')
        comp_point += 1
        time.sleep(2)

    elif comp_choice == 'scissor' and human_choice == 'paper':
        print('you loose this turn!! \n' + f'you chose {human_choice} and the computer chose {comp_choice}')
        comp_point += 1
        time.sleep(2)

    else:

        print('you win this turn!!\n' + f'you chose {human_choice} and the computer chose {comp_choice}')
        human_point += 1
        time.sleep(2)

if human_point > comp_point:
    print(f'your total points are {human_point} and computers total points are {comp_point}')
    print('congrats,you win this game!!!')



elif human_point < comp_point:
    print(f'your total points are {human_point} and computers total points are {comp_point}')
    print('you loose this game!!\n' + f'better luck next time..')


else:
    print(f'your total points are {human_point} and computers total points are {comp_point}')
    print('both have equal points\n the match is drawn..')

    print('thanks for playing!!!')
