from collections import deque

class MyStack(object):

    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)

    def pop(self):
        for i in range(len(self.q)-1):
            self.q.append(self.q.popleft())

        return self.q.popleft()

    def top(self):
        for i in range(len(self.q)-1):
            self.q.append(self.q.popleft())

        x = self.q.popleft()
        self.q.append(x)

        return x

    def empty(self):
        return len(self.q) == 0