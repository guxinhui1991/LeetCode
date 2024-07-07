class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        arr1, arr2 = list(num1), list(num2)
        res = []
        N1, N2 = len(arr1), len(arr2)
        ptr_1, ptr_2 = N1 - 1, N2 - 1
        carry = 0
        while ptr_1 >= 0 or ptr_2 >= 0:
            v1 = ord(arr1[ptr_1]) - ord("0") if ptr_1 >= 0 else 0
            v2 = ord(arr2[ptr_2]) - ord("0") if ptr_2 >= 0 else 0
            v = (v1 + v2 + carry) % 10
            carry = (v1 + v2 + carry) // 10

            res.append(chr(ord("0") + v))
            ptr_1 -= 1
            ptr_2 -= 1

        if carry:
            res.append("1")

        return "".join(res[::-1])

