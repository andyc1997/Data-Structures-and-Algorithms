# python3

def max_pairwise_product(numbers):
    n = len(numbers)
    numbers_copy = numbers
    
    index = 0
    for i in range(1, n):
        if numbers_copy[i] > numbers_copy[index]:
            index = i
            
    index_new = 0
    if index == 0:
        index_new = 1
    
    for i in range(0, n):
        if (i != index) and (numbers_copy[i] > numbers_copy[index_new]):
            index_new = i
    max_product = numbers_copy[index] * numbers_copy[index_new]

    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))