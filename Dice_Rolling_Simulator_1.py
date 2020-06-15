from random import randrange

repeat=True

while repeat:
    dice_number=randrange(1,7)
    print("You Rolled",dice_number)
    print("Press Y or y to continue and any other key to exit")
    rsp=input().strip().lower()
    if rsp=='y':
        continue
    else:
        repeat=False
    print("End of the Game")


