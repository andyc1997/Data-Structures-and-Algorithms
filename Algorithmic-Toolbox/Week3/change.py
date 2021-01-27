# Uses python3
import sys
# Task. The goal in this problem is to find the minimum number of coins needed to change the input value
# (an integer) into coins with denominations 1, 5, and 10.
# Input Format. The input consists of a single integer m.
# Constraints. 1 <= m <= 103.
# Output Format. Output the minimum number of coins with denominations 1, 5, 10 that changes m.

def get_change(m):
    # Greedy algorithm: First change with coins with denomination 10
    # Then, change with coins with denomination 5.
    # At last, change with coins with denomination 1.
    # Safe move: Suppose we have K amount changed using the abovementioned procedure.
    # Suppose we have M additional amount added to K. 
    # We change K + M with (K + M) mod 10 coins denominated with 10.
    # For the subproblem, we must also change K and M with K mod 10 and M mod 10 coins denominated in 10, resp.
    # Hence, it's a safe move to change with coins denominated in 10 first.
    # Second, we can change L = (K + M) mod 10 with L mod 5 coins denominated in 5.
    # For the subproblem, we must also change (K mod 10) mod 5 and (M mod 10) mod 5 for K and M, resp.
    # Hence, it's also a safe move. The remaining amount should therefore be changed with coins denominated in 1.
    # The optimality of subproblem is consistent with the optimality of the original problem.
    after_ten = m % 10 # Total amount after changing with coin 10
    ten_count = (m - after_ten) / 10 # How many coin 10 should be changed
    after_five = after_ten % 5 # Total amount after changing with coin 5, it can be changed with coin 1
    five_count = (after_ten - after_five) / 5 # How many coin 5 should be changed
    m = int(after_five + five_count + ten_count) 
    return m

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
