from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        self.change = {}

        for i in bills:

            self.change[i] = self.change.get(i, 0) + 1
            if i == 10:
                if 5 in self.change:
                    self.change[5]-=1
                    if self.change[5]==0: del self.change[5]
                else:
                    return False
            elif i == 20:
                if 10 in self.change and 5 in self.change:
                    self.change[10]-=1
                    self.change[5]-=1
                    if self.change[10]==0: del self.change[10]
                    if self.change[5]==0: del self.change[5]
                elif self.change.get(5, 0) >= 3:
                    self.change[5]-=3
                    if self.change[5]==0: del self.change[5]
                else:
                    return False


        return True