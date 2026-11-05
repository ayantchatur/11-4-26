class Stack:
    def __init__(self,n):
        self.stack = []
        self.n = n

    def push(self, k):
        if len(self.stack) < self.n:
            self.stack.append(k)
        else:
            print("The stack is full")

    def pop(self):
        if len(self.stack)==0:
            print("The stack is empty.")
            return ""
        else:
            return self.stack.pop(-1)

    def top(self):
        if len(self.stack) == 0:
            print("The stack is empty")
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def display(self):
        print(self.stack)

class Queue:
    def __init__(self,size):
        self.queue = [None]*size
        self.front = 0
        self.rear = 0
        self.size = size
        self.available = size

    def enqueue(self, item):
        if self.available == 0:
            print("Queue Overflow!")
        else:
            self.queue[self.rear] = item
            self.rear = (self.rear + 1) % self.size
            self.available -=1

    def dequeue(self):
        if self.available == self.size:
            print("Queue Underflow")
        else:
            x=self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            self.available +=1
            return x

    def peek(self):
        print(self.queue[self.front])

    def getRear(self):
        print(self.queue[self.rear])

    def print_queue(self):
        print(self.queue)

    def get_size(self):
        print(self.size-self.available)
        return self.size-self.available

reversetsqueue=Queue(5)
reverseintsstack=Stack(5)
for i in range(5):
    reversetsqueue.enqueue((i+1)*10)
reversetsqueue.print_queue()
for i in range(reversetsqueue.get_size()):
    reverseintsstack.push(reversetsqueue.dequeue())
reverseintsstack.display()
for i in range(reverseintsstack.size()):
    reversetsqueue.enqueue(reverseintsstack.pop())
reversetsqueue.print_queue()