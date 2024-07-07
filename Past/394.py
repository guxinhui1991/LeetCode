'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

'''


class Solution:
    def decodeString(self, s: str) -> str:
        tempStack = [""]
        i, num, strLen = 0, 0, len(s)
        while i < strLen:
            if s[i].isdigit():
                num = num*10 + int(s[i])
            elif s[i] == '[':
                tempStack.append(num)
                num = 0
                tempStack.append("")
            elif s[i] == ']':
                str1 = tempStack.pop()
                numRep = tempStack.pop()
                str2 = tempStack.pop()
                tempStack.append(str2+numRep*str1)
            else:
                tempStack[-1] += s[i]

            i += 1
        return tempStack.pop()

print(Solution().decodeString(s='3[a5[c]]4[b]'))