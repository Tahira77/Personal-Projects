def print_board(board):
    print("\n")
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("---|---|---")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("---|---|---")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("\n")

def check_win(board):
    win_conditions = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Horizontal
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Vertical
        (1, 5, 9), (3, 5, 7)              # Diagonal
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return True
    return False

def check_draw(board):
    return all(space != ' ' for space in board[1:])

def tic_tac_toe():
    board = [' '] * 10  # Initialize the board with empty spaces
    current_player = 'X'
    
    while True:
        print_board(board)
        
        try:
            choice = int(input(f"Player {current_player}, enter a number (1-9): "))
            if 1 <= choice <= 9 and board[choice] == ' ':
                board[choice] = current_player
            else:
                print("Invalid move. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        
        if check_win(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            print_board(board)
            print("The game is a draw!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    while True:
        tic_tac_toe()
        replay = input("Do you want to play again? (y/n): ")
        if replay.lower() != 'y':
            break
