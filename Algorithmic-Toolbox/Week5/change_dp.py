# Uses python3
import sys

def get_change(money):
    #write your code here
    coins = [1, 3, 4]
    MinNumCoins = []
    MinNumCoins.append(0)
    
    for m in range(money):
        MinNumCoins.append(money + 1)
        for i in range(len(coins)):
            if m + 1 >= coins[i]:
                NumCoins = MinNumCoins[m + 1 - coins[i]] + 1
                if NumCoins < MinNumCoins[m + 1]:
                    MinNumCoins[m + 1] = NumCoins

    return MinNumCoins[money]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
