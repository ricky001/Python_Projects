from random import randint

def roll_dice(player=1,number_of_games=100):
    roll_numbers={i:0 for i in range(1,7)}
    total_score=0

    for _roll in range(number_of_games):
        random_number = randint(1,6)
        roll_numbers[random_number]=roll_numbers[random_number]+1
        total_score+=random_number
    print(f"Player {player} has done the below rolls \n {roll_numbers}")
    print(f"{'-'*15} \nTotal Score:- {total_score} ")
    return total_score



def print_result(score_1,score_2):
    line = "-"*15
    print(f"{line}\n Results \n {line}")
    if score_1>score_2:
        print("*** Hurray Player 1 won ***")
    elif score_1<score_2:
        print("*** Hurray Player 2 won ***")
    elif score_1==score_2:
        print("*** Tie :) ***")

def play_one_game():
    score1=roll_dice(player=1,number_of_games=100)
    score2=roll_dice(player=2,number_of_games=100)
    print_result(score1,score2)


if __name__ == "__main__":
    play_one_game()
