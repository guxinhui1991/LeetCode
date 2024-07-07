class Solution:
    def reformatDate(self, date: str) -> str:
        arr = date.split(" ")
        res = []
        m = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        j, n = 0, 0

        # date
        while arr[0][j].isdigit():
            n *= 10
            n += int(arr[0][j])
            j += 1
        res.insert(0, str(n) if n > 9 else "0" + str(n))

        # month
        j = m.index(arr[1])
        res.insert(0, str(j + 1) if j >= 9 else "0" + str(j + 1))

        # year
        res.insert(0, arr[-1])
        return "-".join(res)

