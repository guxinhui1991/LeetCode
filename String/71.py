class Solution:
    def simplifyPath(self, path: str) -> str:

        len_path = len(path)
        stack = []

        i = 0
        while i < len_path:
            if path[i] == "/":
                i+=1
                continue

            cur = ""
            while i < len_path and path[i] != "/":
                cur += path[i]
                i += 1

            if cur == ".":
                i += 1
                continue
            elif cur == "..":
                if stack: stack.pop()
            else:
                stack.append(cur)
            i += 1

        return "/" + "/".join(stack)


Solution().simplifyPath("/home/")