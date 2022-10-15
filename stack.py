class Stack:

    def __init__(self):
        self.data = []  #atrybut

    def pop(self):    #metoda
        return self.data.pop()

    def push(self, item):
        self.data.append(item)

    def peek(self):
        return self.data[-1]

if __name__ == "__main__":
    stack = Stack()
    print(stack.data)
    stack.push(10)
    stack.push(20)
    print(stack.peek())
