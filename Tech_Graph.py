import math
import collections

# Add any extra import statements you may need here


# Add any helper functions you may need here


def minOperations(arr):
    # Write your code here
    target = "".join([str(num) for num in sorted(arr)])
    curr = "".join([str(num) for num in arr])
    queue = collections.deque([(0, curr)])  # In the queue we store (<level>, <permutation>)
    visited = set([curr])

    while queue:
        level, curr = queue.popleft()

        if curr == target:
            return level  # We are done

        for i in range(len(curr)):
            for j in range(i, len(curr)):
                # Reverse elements between i and j (inclusive)
                # Note we are operating on strings here, so we create a new copy
                permutation = curr[:i] + curr[i:j + 1][::-1] + curr[j + 1:]

                if permutation not in visited:
                    visited.add(permutation)
                    queue.append((level + 1, permutation))

    return -1


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
    print('[', n, ']', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printInteger(expected)
        print(' Your output: ', end='')
        printInteger(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    n_1 = 5
    arr_1 = [1, 2, 5, 4, 3]
    expected_1 = 1
    output_1 = minOperations(arr_1)
    check(expected_1, output_1)

    n_2 = 3
    arr_2 = [3, 1, 2]
    expected_2 = 2
    output_2 = minOperations(arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
