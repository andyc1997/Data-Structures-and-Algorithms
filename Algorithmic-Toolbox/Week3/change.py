# Uses python3
import sys

def get_change(m):
    #write your code here
    after_ten = m % 10
    ten_count = (m - after_ten) / 10
    after_five = after_ten % 5
    five_count = (after_ten - after_five) / 5
    m = int(after_five + five_count + ten_count)
    return m

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
