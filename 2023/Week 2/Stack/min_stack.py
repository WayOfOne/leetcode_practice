# based on https://leetcode.com/problems/min-stack/
# can't use a min heap/priority queue here since the getMin is supposed to be O(1)

class MinStack:
    
    def __init__(self):
        data = []
        mins = []

    def push(self, val: int) -> None:
        # if the new value is less than the current min, add it to the mins list\
        # otherwise, add the current min to the mins list
        if len(self.mins) == 0 or val < self.mins[-1]:
            self.mins.append(val)
        self.data.append(val)

    def pop(self) -> None:
        # if the value being popped is the current min, pop it from the mins list
        if self.data[-1] == self.mins[-1]:
            self.mins.pop()
        self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.mins[-1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()