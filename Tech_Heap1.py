import math
import heapq

# Add any extra import statements you may need here


# Add any helper functions you may need here


def findMaxProduct(arr):
    # Write your code here

    if len(arr) < 3: return [-1] * len(arr)
    h = []
    heapq.heappush(h, arr[0])
    heapq.heappush(h, arr[1])
    heapq.heappush(h, arr[2])

    resProd = 1
    for i in h:
        resProd = resProd * i

    res = [-1, -1, resProd]
    for i in range(3, len(arr)):
        if arr[i] > h[0]:
            popVal = heapq.heappop(h)
            heapq.heappush(h, arr[i])
            resProd = resProd // popVal * arr[i]
        res.append(resProd)

    return res


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
    print('[', n, ']', sep='', end='')


def printIntegerList(array):
    size = len(array)
    print('[', end='')
    for i in range(size):
        if i != 0:
            print(', ', end='')
        print(array[i], end='')
    print(']', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    expected_size = len(expected)
    output_size = len(output)
    result = True
    if expected_size != output_size:
        result = False
    for i in range(min(expected_size, output_size)):
        result &= (output[i] == expected[i])
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printIntegerList(expected)
        print(' Your output: ', end='')
        printIntegerList(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    arr_1 = [1, 2, 3, 4, 5]
    expected_1 = [-1, -1, 6, 24, 60]
    output_1 = findMaxProduct(arr_1)
    check(expected_1, output_1)

    arr_2 = [2, 4, 7, 1, 5, 3]
    expected_2 = [-1, -1, 56, 56, 140, 140]
    output_2 = findMaxProduct(arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
