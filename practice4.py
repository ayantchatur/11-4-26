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

whoknewabttsqueue=Queue(10)
for i in range(5):
    whoknewabttsqueue.enqueue((i+1)*10)
whoknewabttsqueue.get_size()