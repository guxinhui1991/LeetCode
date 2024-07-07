class TwoSum:

    def __init__(self):
        self.cur = {}

    def add(self, number: int) -> None:
        self.cur[number] = self.cur.get(number, 0) + 1

    def find(self, value: int) -> bool:
        for k, v in self.cur.items():
            if value - k != k and value - k in self.cur:
                return True
            elif value - k == k:
                if v >= 2: return True

        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)