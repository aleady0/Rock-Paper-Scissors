# Write your code here
import os.path
import random


ratings = dict()
rating_file_name = 'rating.txt'
if os.path.exists(rating_file_name):
    rating_file = open(rating_file_name, 'r')
    for line in rating_file:
        k, v = line.split(' ')
        ratings[k] = int(v)
    rating_file.close()    

user_name = input('Enter your name:')
print('Hello, {}'.format(user_name))

choises_input = input()
if len(choises_input) == 0:
    choises = {'paper':['scissors'], 'scissors':['rock'], 'rock':['paper']}
else:
    choises = dict()
    choises_list = choises_input.split(',')
    for k, v in enumerate(choises_list):
        nl = choises_list[:k] + choises_list[k+1:]
        l = len(nl)
        choises[v] = nl[0:l//2]    
print("Okay, let's start")
while True:
    user_choise = input()
    if user_choise == '!exit':
        print('Bye!')
        with open(rating_file_name, 'w') as f:
            for k in ratings:
                f.write(k + ' ' + str(ratings[k]))
        break
    elif user_choise == '!rating':
        print('Your rating: {}'.format(ratings[user_name]))
        continue    
    elif user_choise not in choises:
        print('Invalid input')
        continue
    computer_choise = random.choice(list(choises))
    if user_choise == computer_choise:
        print('There is a draw ({})'.format(computer_choise))
        result = 50
    elif computer_choise in choises[user_choise]:
        print('Sorry, but computer chose {}'.format(computer_choise))
        result = 0
    else:
        print('Well done. Computer chose {} and failed'.format(computer_choise))
        result = 100
    ratings[user_name] = ratings.get(user_name,0) + result 
