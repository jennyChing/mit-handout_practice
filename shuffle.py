import random
def shuffle(cards):
    for i in range(0,len(cards)):
        ran = random.randint(i,len(cards)-1)
        cards[i], cards[ran] = cards[ran], cards[i]
while True:
    try:
        cards = list(map(int, input().split()))
        shuffle(cards)
        print(cards)
    except(EOFError):
        break
