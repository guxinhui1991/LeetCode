class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        count ={}
        for i in magazine:
            count[i] = count.get(i, 0) + 1

        for i in ransomNote:
            if i not in count:
                return False
            else:
                count[i]-=1

        return all(x>=0 for _,x in count.items())