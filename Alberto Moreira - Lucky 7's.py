# generate two random numbers
# print on next line
import random
money = 15
wins = 0
lose = 0
rounds = 0
most = money
while money > 0:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(dice1)
    print(dice2)
    total = dice1 + dice2
    print(total)
    if total == 7:
        money += 4
        wins += 1
        if most < money:
         most = money
        print(most)
    else:
        money -= 1
        print(money)
        lose += 1
    rounds += 1

print("wins %s" % wins)
print("lose %s" % lose)
print("rounds %s" % rounds)
print(most)
