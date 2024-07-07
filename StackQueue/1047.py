class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        cur_stack = []
        cur_stack_index = []
        str_arr = list(s)
        for i, c in enumerate(str_arr):
            if not cur_stack or c != cur_stack[-1]:
                cur_stack.append(c)
                cur_stack_index.append(i)
            else:
                cur_stack.pop()
                str_arr[cur_stack_index.pop()] = ""
                str_arr[i] = ""

        return "".join(str_arr)

Solution().removeDuplicates("abbaca")