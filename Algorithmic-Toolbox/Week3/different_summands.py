# Uses python3
import sys
# Task. You are organizing a funny competition for children. As a prize fund you have n
# candies. You would like to use these candies for top k places in a competition
# with a natural restriction that a higher place gets a larger number of candies.
# To make as many children happy as possible, you are going to find the largest
# value of k for which it is possible.
# Task. The goal of this problem is to represent a given positive integer n as a sum of as many pairwise
# distinct positive integers as possible. That is, to find the maximum k such that n can be written as
# a[1] + a[2] + · · · + a[k] where a[1], . . . , a[k] are positive integers and a[i] != a[j] for all 1 <= i < j <= k.
# Input Format. The input consists of a single integer n.
# Output Format. In the first line, output the maximum number k such that n can be represented as a sum
# of k pairwise distinct positive integers. In the second line, output k pairwise distinct positive integers
# that sum up to n (if there are many such representations, output any of them).

# Greedy algorithm: We are going to express n in terms of k increasing integers and maximize k. 
# If there are more than 2 candies, we add 1, 2, 4, 6, ... 2*k until the remaining candies are less than 2*(k + 1)
# Then, we distribute the remaining candies to 1 place in the competition.
def optimal_summands(n):
    summands = []
    n_sum = n
    choice = 1
    while n_sum > 2*choice:
        summands.append(choice)
        n_sum -= choice
        choice += 1
    
    summands.append(n_sum)
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
