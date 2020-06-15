from random import randint

def roll_dice(number_of_games=100):
    roll_numbers1={i:0 for i in range(1,7)}
    roll_numbers2={i:0 for i in range(1,7)}
    total_score1=0
    total_score2=0
    counter=0
    while True:
        
        randome_number1=randint(1,6)
        roll_numbers1[randome_number1]+=1
        total_score1+=randome_number1

        
        randome_number2=randint(1,6)
        roll_numbers2[randome_number2]+=1
        total_score2+=randome_number2
        if total_score1==total_score2:
            counter+=1
            print(f"The number of rolls rolled {counter}")
            print(f"Player1 has done the below rolls \n {roll_numbers1}")
            print(f"Player2 has done the below rolls \n {roll_numbers2}")
            break
        else:
            counter+=1
            continue
        


   





def play_one_game():
    roll_dice(number_of_games=100)
    


if __name__ == "__main__":
    play_one_game()
