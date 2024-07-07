class Solution:
    def __init__(self):
        self.dic = {}
        self.dic[1] = "1"

    def countAndSay(self, n: int) -> str:
        if n in self.dic: return self.dic[n]
        cur = self.countAndSay(n - 1)

        ptr = 0
        count = []
        while ptr < len(cur):
            c = cur[ptr]
            n = 1
            ptr += 1
            while ptr < len(cur) and cur[ptr] == c:
                ptr += 1
                n += 1
            count.append(str(n) + c)

        self.dic[n] = "".join(count)
        return self.dic[n]

print(Solution().countAndSay(1))
print(Solution().countAndSay(2))
print(Solution().countAndSay(3))
print(Solution().countAndSay(4))