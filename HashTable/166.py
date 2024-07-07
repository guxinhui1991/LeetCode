class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return "0"
        if denominator == 0: return False

        res = []
        if numerator * denominator < 0:
            res += "-"
            numerator, denominator = abs(numerator), abs(denominator)

        frac = numerator // denominator
        rem = numerator % denominator

        res.append(str(frac))
        if rem == 0: return "".join(res)

        dig_pos = {}
        res.append(".")
        while rem:
            if rem in dig_pos:
                res.insert(dig_pos[rem], "(")
                res.append(")")
                break
            dig_pos[rem] = len(res)
            rem *= 10
            res.append(str(rem//denominator))
            rem = rem%denominator

        return "".join(res)

print(Solution().fractionToDecimal(1, 2))
print(Solution().fractionToDecimal(1, 3))
