# Feb 9, 2022
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

# Dec 14, 2022
class Solution2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count ={}
        for i in s:
            count[i] = count.get(i, 0) + 1

        for i in t:
            if i not in count:
                return False
            else:
                count[i]-=1
                if count[i] ==0: del count[i]

        return count == {}

class Solution3(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import Counter
        a_count = Counter(s)
        b_count = Counter(t)
        return a_count == b_count


s = "anagram"
t = "nagaram"

print(Solution2().isAnagram(s, t))