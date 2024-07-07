def CommonSuffix(s: str) -> str:
    N = len(s)
    dp = [0] * N

    for i in range(1, N):
        j = dp[i-1]
        while j >= 1 and s[j] != s[i]:
            j = dp[j-1]
        dp[i] = j + (s[j] == s[i])

    return dp



def KMP(haystack: str, needle: str) -> str:

    N, M = len(haystack), len(needle)

    dp = [0] * N
    suffix = CommonSuffix(needle)

    if M == 0: return 0
    if N == 0: return -1

    dp[0] = haystack[0] == needle[0]
    if M == 1 and dp[0] == 1: return 0

    ################################################################################
    #
    # j = dp[i] means needle[:j-1] == haystack[i-j+1 : i]
    #
    ################################################################################

    for i in range(1, N):
        j = dp[i-1]
        while j >= 1 and haystack[i] != needle[j]:
            j = suffix[j-1]
        dp[i] = j + (haystack[i] == needle[j])

        if dp[i] == M: return i-M+1

    return -1




if __name__ == "__main__":

    haystack = "leet"
    needle = "eet"
    print(KMP(haystack, needle))
    haystack = "sadbutsad"
    needle = "sad"
    print(KMP(haystack, needle))

