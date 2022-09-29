import random


def roll():
  response = 'y'

  while response == 'y':
    num = random.randint(1,6)
    if num == 1:
      print('[-----]')
      print('[     ]')
      print('[  0  ]')
      print('[     ]')
      print('[-----]')

      tmp = input("Would you like to roll again? (y or n): ")
      response = tmp

      #return 1
    elif num == 2:
      print('[-----]')
      print('[0    ]')
      print('[     ]')
      print('[    0]')
      print('[-----]')
      
      tmp = input("Would you like to roll again? (y or n): ")
      response = tmp

      #return 2
    elif num == 3:
      print('[-----]')
      print('[0    ]')
      print('[  0  ]')
      print('[    0]')
      print('[-----]')

      tmp = input("Would you like to roll again? (y or n): ")
      response = tmp

      #return 3
    elif num == 4:
      print('[-----]')
      print('[0   0]')
      print('[     ]')
      print('[0   0]')
      print('[-----]')
      
      tmp = input("Would you like to roll again? (y or n): ")
      response = tmp

      #return 4 
    elif num == 5:
      print('[-----]')
      print('[0   0]')
      print('[  0  ]')
      print('[0   0]')
      print('[-----]')
      
      tmp = input("Would you like to roll again? (y or n): ")
      response = tmp

      #return 5 
    elif num == 6:
      print('[-----]')
      print('[0   0]')
      print('[0   0]')
      print('[0   0]')
      print('[-----]')
      
      tmp = input("Would you like to roll again? (y or n): ")
      response = tmp

      #return 6

  return

roll()


