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
reverseTs = input("yo what do u wanna reverse\n")

reversingStack = Stack(len(reverseTs))
for i in reverseTs:
    reversingStack.push(i)

reversedTs=""
for i in reverseTs:
    reversedTs+= reversingStack.pop()
print("reversed:\n"+reversedTs)