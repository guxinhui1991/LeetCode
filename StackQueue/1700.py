import collections
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        while sandwiches and students:
            if students[0] != sandwiches[0]:
                students.append(students.pop(0))

            while students and sandwiches and students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)

            if len(set(students)) == 1 and students[0] != sandwiches[0]:
                return len(students)

        return len(students)


    # Lee215
    def countStudents2(self, students, sandwiches):
        count = collections.Counter(students)
        n, k = len(students), 0
        while k < n and count[sandwiches[k]]:
            count[sandwiches[k]] -= 1
            k += 1
        return n - k

Solution().countStudents2(students= [1, 1, 0, 0], sandwiches= [0, 1, 0, 1])