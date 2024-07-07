class MyCircularQueue:

    def __init__(self, k: int):
        self.val = []
        self.max_size = k

    def enQueue(self, value: int) -> bool:
        if not self.val or len(self.val) < self.max_size:
            self.val.append(value)
            return True
        else:
            return False


    def deQueue(self) -> bool:
        if self.val:
            self.val.pop(0)
            return True
        else:
            return False

    def Front(self) -> int:
        if not self.val: return -1
        return self.val[0]

    def Rear(self) -> int:
        if not self.val: return -1
        return self.val[-1]

    def isEmpty(self) -> bool:

        return not self.val

    def isFull(self) -> bool:
        if not self.val: return False
        return len(self.val) == self.max_size

myCircularQueue = MyCircularQueue(3)
print(myCircularQueue.enQueue(1))
print(myCircularQueue.enQueue(2))
print(myCircularQueue.enQueue(3))
print(myCircularQueue.enQueue(4))
print(myCircularQueue.Rear())
print(myCircularQueue.isFull())
print(myCircularQueue.deQueue())
print(myCircularQueue.enQueue(4))
print(myCircularQueue.Rear())
