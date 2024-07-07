class Solution:

    # Using dict
    def buddyStrings0(self, s: str, goal: str) -> bool:

        if len(s) != len(goal): return False

        N = len(s)

        count = 0
        s_dict, g_dict = {}, {}
        for i in range(N):
            if s[i] != goal[i]: count += 1

            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
            g_dict[goal[i]] = g_dict.get(goal[i], 0) + 1

        for k, v in g_dict.items():
            if k not in s_dict or s_dict[k] != v: return False

        if (count > 2) or (count == 0 and all(i < 2 for i in s_dict.values())):
            return False

        return True

    # Using index
    def buddyStrings1(self, s: str, g: str) -> bool:
        if len(s) != len(g): return False

        c = [0 for _ in range(26)]
        if s == g:
            for i in s:
                c[ord(i) - ord('a')] += 1
                if c[ord(i) - ord('a')] == 2: return True
            return False

        l1 = l2 = -1
        s1 = set()
        s2 = set()
        for i in range(len(s)):
            if s[i] != g[i]:
                if l1 == -1:
                    l1 = i
                    s1.add(s[i])
                    s2.add(g[i])
                elif l2 == -1:
                    l2 = i
                    s1.add(s[i])
                    s2.add(g[i])
                else:
                    return False

        if l2 == -1 or s1 != s2: return False
        return True
