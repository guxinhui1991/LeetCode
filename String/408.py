class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        t = [c for c in abbr]
        len_w, len_t = len(word), len(t)
        ptr_t, ptr_w = 0, 0

        while ptr_w < len_w and ptr_t < len_t:

            start_t = ptr_t
            if str.isnumeric(t[ptr_t]):
                if int(t[start_t]) == 0: return False
                while ptr_t<len_t and str.isnumeric(t[ptr_t]):
                    ptr_t += 1
                ptr_w += int("".join(t[start_t:ptr_t]))
                continue


            if word[ptr_w] != t[ptr_t]:
                return False
            ptr_w += 1
            ptr_t += 1

        return True if ptr_t == len_t and ptr_w == len_w else False


class Solution2:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        a, b = 0, 0
        c = 0
        while a < len(word) and b < len(abbr):
            if abbr[b].isdigit():
                c = c*10 + int(abbr[b])
                if c == 0: return False
                b+=1
            else:
                a += c
                if a>=len(word) or word[a] != abbr[b]: return False
                a += 1
                b += 1
                c = 0
        a += c
        return True if a == len(word) and b == len(abbr) else False

print(Solution().validWordAbbreviation("aa", "2"))
print(Solution2().validWordAbbreviation(word="aa", abbr="2"))
print(Solution().validWordAbbreviation("internationalization", "i5a11o1"))
print(Solution2().validWordAbbreviation(word="internationalization", abbr="i5a11o1"))
print(Solution2().validWordAbbreviation(word = "internationalization", abbr = "i12iz4n"))
print(Solution2().validWordAbbreviation(word = "apple", abbr = "a2e"))