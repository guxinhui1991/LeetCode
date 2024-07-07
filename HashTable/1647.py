class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """

        count_dict = {}
        for i in s:
            if i in count_dict.keys():
                count_dict[i] += 1
            else:
                count_dict[i] = 1


        cur_set = set()
        count = 0
        for i in count_dict.keys():
            freq = count_dict[i]
            while(freq > 0 and freq in cur_set):
                freq -= 1
                count +=1
            cur_set.add(freq)
        return count

