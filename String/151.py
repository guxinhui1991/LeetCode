class Solution(object):
    # Dec 2023
    # O(n) additional space
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """


        s_reversed = s[::-1]

        s_list = s_reversed.split(' ')
        s_list = [e for e in s_list if e.strip()]
        return ' '.join(s[::-1] for s in s_list)


    def reverseWords2(self, s):
        """
        :type s: str
        :rtype: str
        """


        i = 0
        words = s.split()
        s = self.reverseList(words)

        return " ".join(s)

    def reverseList(self, s):

        l, r = 0, len(s)-1

        while l < r:
            tmp = s[l]
            s[l] = s[r]
            s[r] = tmp

            l += 1
            r -= 1
        return s
print(Solution().reverseWords(r'a good   example'))
print(Solution().reverseWords2(r'a good   example'))