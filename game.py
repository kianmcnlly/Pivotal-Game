import os

def help_menu():
    print('hi')
def start_game():
    print('hello')
def options():
  options_choice = input(">").lower().strip()
  if options_choice  == "play":
    start_game()
  elif options_choice== "help":
    help_menu()
  elif options_choice == "quit":
    os.system("cls")
  else:
    print("Invalid input")
    options_choice()

def options_menu():
  print("##########################")
  print("   Welcome to Mikado      ")
  print("##########################")
  print("          ·Play·          ")
  print("          ·Help·          ")
  print("          ·Quit·          ")
  options()
options_menu()
class player:
    def within(self):
        self.name = ''
        self.hp = 100
        self.status = []
    mycharacter = player()
def map():
    area_map:{
        floor1 :{
            a1:{
            up = '',
            down = 'a2',
            left = '',
            right =  'b1',
            examine == '',
            description == '',
            },
            a2:{
            up = 'a1',
            down = 'a3',
            left = '' ,
            right = 'b2',
            examine == '',
            description == '',
            },
            a3:{
            up = 'a2',
            down = 'a4',
            left = '',
            right = '',
            examine == '',
            description == '',
            },
            a4:{
            up = 'a3',
            down = 'a5',
            left = '',
            right = '',
            examine == '',
            description == '',
            },
            a5:{
            up = 'a4',
            down = '',
            left = '',
            right = 'b5',
            examine == '',
            description == '',
            },
            a7:{
            up = '',
            down = '',
            left = '',
            right = 'b7',
            examine == '',
            description == '',
            },
            b1:{
            up = '',
            down = 'b2',
            left = 'a1',
            right = '',
            examine == '',
            description == '',
            },
            b2:{
            up = 'b1',
            down = '',
            left = 'a2',
            right = 'c2',
            examine == '',
            description = '',
            },
            b5:{
            up = '',
            down = '',
            left = 'a5',
            right = '',
            examine = '',
            description = '',
            },
            b7:{
            up = '',
            down = '',
            left = 'a7',
            right = 'c7',
            examine = '',
            description = '',
            },
            c2:{
            up = '',
            down = 'c3',
            left = 'b2',
            right = '',
            examine = '',
            description = '',
            },
            c3:{
            up = 'c2',
            down = '',
            left = '',
            right = 'd3',
            examine = '',
            description = '',
            },
            c7:{
            up = '',
            down = '',
            left = 'b7',
            right = 'd7',
            examine = '',
            description = '',
            },
            d3:{
            up = '',
            down = 'd4',
            left = 'c3',
            right = '',
            examine = '',
            description = '',
            },
            d4:{
            up = 'd3',
            down = 'd5',
            left = '',
            right = '',
            examine = '',
            description = '',
            },
            d5:{
            up = 'd4',
            down = 'd6',
            left = '',
            right = '',
            examine = '',
            description = '',
            },
            d6:{
            up = 'd5',
            down = 'd7',
            left = '',
            right = 'e6',
            examine = '',
            description = '',
            },
            d7:{
            up =  'd6',
            down = '',
            left = 'c7',
            right = 'e7',
            examine = '',
            description = '',
            },
            e6:{
            up = '',
            down = 'e7',
            left = 'd6',
            right = 'f6',
            examine = '',
            description = '',
            },
            e7:{
            up = 'e6',
            down = '',
            left = 'd7',
            right = 'g7',
            examine = '',
            description = '',
            },
            f1:{
            up = 'floor2',
            down = 'f2',
            left = '',
            right = '',
            examine = '',
            description = '',
            },
            f2:{
            up = 'f1',
            down = 'f3',
            left = '',
            right = '',
            examine = '',
            description = '',
            },
            f3:{
            up = 'f2',
            down = 'f4',
            left = '',
            right = '',
            examine = '',
            description = '',
            },
            f4:{
            up = 'f3',
            down = 'f5',
            left =  '',
            right = '',
            examine = '',
            description = '',
            },
            f5:{
            up = 'f4',
            down = 'f6',
            left = '',
            right = '',
            examine = '',
            description = '',
            },
            f6:{
            up = 'f5',
            down = 'f7',
            left = 'e6',
            right = 'g7',
            examine = '',
            description = '',
            },
            f7:{
            up = 'f6',
            down = '',
            left = 'e7',
            right = 'g7',
            examine = '',
            description = '',
            },
            g6:{
            up = '',
            down = 'g7',
            left = 'f6',
            right = 'h6',
            examine = '',
            description = '',
            },
            g7:{
            up = 'g6',
            down = '',
            left = 'f7',
            right = 'h7',
            examine = '',
            description = '',
            },
            h1:{
            up = '',
            down = 'h2',
            left = '',
            right = '',
            examine = '',
            description = '',
            },
            h2:{
            up = 'h1',
            down = 'h2',
            left = '',
            right = '',
            examine = '',
            description = '',
            },
            h3:{
            up = 'h2,',
            down = 'h3',
            left = '',
            right = '',
            examine = '',
            description = '',
            },
            h4:{
            up = 'h3',
            down = 'h5',
            left = '',
            right = '',
            examine = '',
            description = '',
            },
            h5:{
            up = 'h4',
            down = 'h6',
            left = '',
            right = '',
            examine = '',
            description = '',
            },
            h6:{
            up = 'h5',
            down = 'h7',
            left = 'g6',
            right = '',
            examine = '',
            description = '',
            },
            h7:{
            up = 'h6',
            down = '',
            left = 'g7',
            right = ','
            examine = '',
            description = '',
            }
          }
        }
def print_location():
    print('\n' + ('#' * (4 + len(mycharacter.location))))
    print('#' + mycharacter.location.upper() + '#')
    print('#' + area_map[mycharacter.postion][description] + '#')
    print('\n' + ('#' * (4 + len(mycharacter.location))))

def actions():
    print('-------------------------------------')
    print('What would you like to do?')
    action = input('>')
    acceptable_actions = ['travel','move','walk','quit','interact','examine','inspect',]
