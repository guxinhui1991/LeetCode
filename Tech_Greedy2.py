import math


# Add any extra import statements you may need here


# Add any helper functions you may need here


def findMinArray(arr, k):
    # Write your code here
    sortIdx = []
    for i in range(len(arr) - 1):
        if arr[i + 1] < arr[i]:
            sortIdx.append(i+1)

    while k > 0 and len(sortIdx) > 0:
        idxToSwap = findMinIndx([x for x in sortIdx if x <= k], arr)
        sortIdx.remove(idxToSwap)

        if idxToSwap > 0:
            arr[idxToSwap]
        arr = [arr[idxToSwap]] + arr[:idxToSwap] + arr[idxToSwap+1:]
        k = k - idxToSwap
        continue

        '''
        idxToSwap = sortIdx.pop(0)
        arr = swapByIndex(arr, idxToSwap, idxToSwap+1)
        k = k - 1
        if idxToSwap + 1 < len(arr)  and arr[idxToSwap] > arr[idxToSwap + 1]:
            sortIdx.insert(0, idxToSwap)
        '''

    return arr

def findMinIndx(idxList, arr):
    if not arr: return None
    res = idxList[0]
    for i in idxList:
        if arr[i] < arr[res]:
            res = i

    return res

def swapByIndex(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

    return arr



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
    n_1 = 3
    arr_1 = [5, 3, 1]
    k_1 = 2
    expected_1 = [1, 5, 3]
    output_1 = findMinArray(arr_1, k_1)
    check(expected_1, output_1)

    n_2 = 5
    arr_2 = [8, 9, 11, 2, 1]
    k_2 = 3
    expected_2 = [2, 8, 9, 11, 1]
    output_2 = findMinArray(arr_2, k_2)
    check(expected_2, output_2)

    # Add your own test cases here
    n_3 = 8
    arr_3 = [5,4,4,6,1,7,9,3]
    k_3 = 3
    expected_3 =  [4,4,5,1,6,7,9,3]
    output_3 = findMinArray(arr_3, k_3)
    check(expected_3, output_3)
