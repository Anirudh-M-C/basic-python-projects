board=['-']*10
computer='o'
human='x'

def display_board(board):
    print(f"{board[1]} | {board[2]} | {board[3]}")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print(f"{board[7]} | {board[8]} | {board[9]}")
    print("-"*10)


def check_win():
        if board[1] == board[2] == board[3] and board[1] != '-':
            return True
        elif board[4] == board[5] == board[6] and board[4] != '-':
            return True
        elif board[7] == board[8] == board[9] and board[7] != '-':
            return True
        elif board[1] == board[4] == board[7] and board[1] != '-':
            return True
        elif board[2] == board[5] == board[8] and board[2] != '-':
            return True
        elif board[3] == board[6] == board[9] and board[3] != '-':
            return True
        elif board[1] == board[5] == board[9] and board[1] != '-':
            return True
        elif board[7] == board[5] == board[3] and board[7] != '-':
            return True
        else:
            return False
        
        
def is_win(letter):
        if board[1] == board[2] == board[3] and board[1] == letter:
            return True
        elif board[4] == board[5] == board[6] and board[4] == letter:
            return True
        elif board[7] == board[8] == board[9] and board[7] == letter:
            return True
        elif board[1] == board[4] == board[7] and board[1] == letter:
            return True
        elif board[2] == board[5] == board[8] and board[2] == letter:
            return True
        elif board[3] == board[6] == board[9] and board[3] == letter:
            return True
        elif board[1] == board[5] == board[9] and board[1] == letter:
            return True
        elif board[7] == board[5] == board[3] and board[7] == letter:
            return True
        else:
            return False
        
        
def check_tie():
    if board.count("-")<2:
    #if '-' not in board:
        return True
    else:
        return False
    
        
def is_available(pos):
    if board[pos]=='-':
        return True 
    else:
        return False
    

def insert(letter,pos):
    if is_available(pos):
        board[pos]=letter
        display_board(board)
        if check_win():
            if letter=='x':
                print("human wins")
            else:
                print("computer wins")
        if check_tie():
            print("tie")
    else:
        pos=int(input("already an element in that position\nenter the position to insert: "))
        insert(letter,pos)


def human_move(letter): #can put letter or human .just putting arg
    pos=int(input("enter the position to insert: "))
    insert(letter,pos)


def computer_move(letter):
    best_score=-100
    best_pos=0
    for index in range(1,len(board)):
        if is_available(index):
            board[index]=letter
            score=minimax(board,False)
            board[index]="-"
            if score>best_score:
                best_score=score
                best_pos=index
    insert(letter,best_pos)
    return


def minimax(board,is_maximizing):
    if is_win(computer):
        return 10
    elif is_win(human):
        return -10
    elif check_tie():
        return 0
    if is_maximizing: 
        best_score=-100
        for index in range(1,len(board)):
            if is_available(index):
                board[index]=computer
                score=minimax(board,False)
                board[index]="-"
                best_score=max(best_score,score)
        return best_score
    else: 
        best_score=100
        for index in range(1,len(board)):
            if is_available(index):
                board[index]=human
                score=minimax(board,True)
                board[index]="-"
                best_score=min(best_score,score)
        return best_score


while not check_win():
    display_board(board)
    computer_move(computer)
    human_move(human)
    

