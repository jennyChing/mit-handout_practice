import random
def flipCoin():
    return random.randint(0,1)
if __name__ == "__main__":
    first = flipCoin()
    second= flipCoin()
    third = flipCoin()
    print(first,second,third)
    dice = 2*2*first+2*second+third
    if dice in range(1,7):
        print(dice)
