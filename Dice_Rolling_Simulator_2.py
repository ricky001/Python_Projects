from random import randint

counter=1
while True:
    random_number =randint(1,6)
    print(f"Rolls {counter} to get {random_number}")
    if random_number==4:
        
        break
    counter+=1