from sortedcontainers import SortedList

'''

We need a data structure that keeps elements sorted and supports fast insertion.

In Java, a TreeMap is the perfect candidate.
In C++, we can use set container and lower_bound method.
In Python, we can keep a SortedList.

'''
class MyCalendar:

    def __init__(self):
        self.meeting = SortedList()

    def book(self, s: int, e: int) -> bool:
        if not self.meeting:
            self.meeting.add((s, e))
            return True
        else:

            idx = self.meeting.bisect((s, e))
            if (idx > 0 and self.meeting[idx - 1][1] > s): return False
            if (idx < len(self.meeting) and self.meeting[idx][0] < e): return False
            self.meeting.add((s, e))
            return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)