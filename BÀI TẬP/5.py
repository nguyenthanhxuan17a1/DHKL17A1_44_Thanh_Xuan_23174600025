class Stack:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.stack = []          
        self.top = -1        
    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity - 1

    def push(self, value):
        if self.isFull():
            print("Ngăn xếp đầy!")
        else:
            self.stack.append(value)  
            self.top += 1             

    def pop(self):
        if self.isEmpty():
            print("Ngăn xếp rỗng!")
            return None
        else:
            self.top -= 1             
            return self.stack.pop() 

    def count(self):
        return self.top + 1 
stack = Stack(5) 
stack.push(2.5)   
stack.push(1.3)   
print(stack.pop())  
print(stack.isEmpty())  
print(stack.count())  
