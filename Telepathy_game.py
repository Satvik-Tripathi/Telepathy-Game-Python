# Telepathy Game with computer

import random
import os  

points=0
print('Welcome to Telepathy Game with computer🖥️')
print('For every match you get 1 point')
print('Best of luck !!')
      
fruits=['apple', 'banana', 'orange', 'mango', 'grapes', 'kiwi', 'pineapple', 'watermelon', 'papaya', 'strawberry']

comp_fruits=random.choice(fruits)

print(f'\nChoose your fav fruit🍒 from {fruits}')
user_fruit=str(input('Enter a Fruit : ')).lower()
if not(user_fruit in fruits):
    print('\nPlease choose from the list above !\n')
else:
  print(f'Computer chose : {comp_fruits} and you chose : {user_fruit}')
  if comp_fruits==user_fruit:
      print('Its a Match ✅')
      points+=1
  else:
     print('\nOops Its not a match❌') 
print(f'\nPoints after this round is {points}')

choco=['dairy milk', 'kitkat', 'perk', '5 star', 'munch', 'ferrero rocher', 'snickers', 'milkybar', 'bournville', 'toblerone']
print(f'\nChoose your fav chocolate🍫 from {choco}')
user_choco=str(input('\nEnter a Chocolate : ')).lower()
comp_choco=random.choice(choco)
if not(user_choco in choco):
   print('Please choose from the list above !')
else:
 print(f'\nComputer chose : {comp_choco} and you chose : {user_choco}')
 if comp_choco==user_choco:
   print('\nIts a Match ✅')
   points+=1
 else:
  print('\nOops Its not a match❌') 
print(f'\nPoints after this round is {points}')
game=['minecraft', 'gta v', 'valorant', 'fortnite', 'pubg', 'counter strike', 'call of duty', 'fifa 23', 'elden ring', 'assassin\'s creed']
print(f'\nChoose your fav game🎮 from {game}')
user_game=str(input('\nEnter a game : ')).lower()
comp_game=random.choice(game)
if not(user_game in game):
   print('\nPlease choose from the list above !')
else:
 print(f'\nComputer chose : {comp_game} and you chose : {user_game}')
 if comp_game==user_game:
   print('\nIts a Match ✅')
   points+=1
 else:
  print('\nOops Its not a match❌')
 
print(f'\nYour total points after all rounds : {points}')

if not(os.path.exists('telepathy_hiscore.txt')):
  with open('telepathy_hiscore.txt','w') as f:
    f.write('')
with open('telepathy_hiscore.txt') as f: 
 hiscore=f.read()               
if hiscore!='': 
    hiscore=int(hiscore)
else:
    hiscore=0   
if   hiscore<points: 
  with open('telepathy_hiscore.txt','w') as f:
    f.write(str(points))
  print(f'High Score : {points}')
else:
   print(f'High Score : {hiscore}')