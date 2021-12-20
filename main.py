from dice import Dice
from win_validator import WinChecker

game_in_session = True  # Flag to track game

def play_game(answer):
    """
    Function to play a game of Greed. 
    As long as the user answers with yes, then a game is played.
    If the user answers with no, then the game is not played.
    """
    global game_in_session

    if (answer.upper() == "YES"):
        greedy = Dice()
        greedy.roll_dice()
        
        greedy_wins = WinChecker(greedy.get_totals())
        greedy_wins.verify_wins()
        print('<------------------->')

    else:
        print("Thank you for playing Greedy.")
        print('<------------------->')
        game_in_session = False
        

if __name__ == "__main__":
    while game_in_session:
        ask_user = input("Would you like to roll the dice? \nYes to play, No to decline\n")
        play_game(ask_user)
        