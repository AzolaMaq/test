# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
board=[
       ["-","-","-"],
       ["-","-","-"],
       ["-","-","-"]
       ]

user=True

def print_row(boards):
    for row in board:
        for slot in row:
            print(slot, end=" ")
        print()




def quit(user_input):
    if user_input.lower() =="q": 
        print("Thanks for playing") 
        return True 
    else: return False

def check_input(user_input):
    if not isnum(user_input): return False
    user_input=int(user_input)
    if not bound(user_input): return False
    return True

def isnum(user_input):
    if not user_input.isnumeric():
        print("not a number")
        return False
    else: return True

def bound(user_input):
    if user_input>9 or user_input<1 :
        print("out of bounds") 
        return False
    else: return True 


def istaken(coords, board):
    row=coords[0]
    col=coords[1]
    if board[row][col] != "-":
        print("already taken")
        return True
    else: return False

def coordinates(user_input):
    row= int(user_input / 3)
    col= user_input
    if col>2: col =int(col % 3)
    return(row,col)
    

def add_to_board(coords,board,active_user):
    row =coords[0]
    col=coords[1]
    board[row][col]=active_user


def current_user(user):
    if user: return "x"
    else: return "o"


def iswin (user,board):
    if checkrow(user,board): True
    
def checkrow(user,board):
    for row in board:
        complete_row= True
        for slot in row:
            if slot != user:
                complete_row=False
                break
        if complete_row: return True
    return False

    
    



while True:
    active_user=current_user(user)
    print_row(board)
    user_input=input("please enter a position, 1 through 9 or enter \"q\" to quit : ")
    if quit(user_input): break

    if not check_input(user_input):
        print("please try again")
        continue
    user_input=int(user_input)-1
    coords=coordinates(user_input)
    
    if istaken(coords, board):
        print("please try again")
        continue
    add_to_board(coords,board,active_user)
    
    if iswin(active_user,board):
        print(f"{active_user.upper()} won")
        break
     
    user=not user