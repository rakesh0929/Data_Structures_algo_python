
class Stack():                               # LIFO - LAST IN FIRST OUT
    def __init__(self) -> None:
        self.data = []
        self.iter = 0
    def isEmpty(self):
        return self.data == []
    def push(self,data):
        self.iter += 1
        self.data.insert(self.iter,data)
        return "The data is added to the stack  : {} ".format(data)
    def pop(self):
        if self.isEmpty() == True:
            print("This Stack has no values sorry")
        else:
            self.iter -=1
            s = self.data.pop(self.iter)
            return "The value popped is : {}".format(s)
    def lis(self):
        print(self.data)
    def len_(self):
        return "The length of the stack is : {}".format(len(self.data))
    
l = Stack()
l.lis()
print(l.isEmpty())
print(l.push(2))
print(l.push(3))
print(l.push(4))
print(l.push(5))
l.lis()
print(l.pop())
l.lis()
print(l.len_())
print(l.isEmpty())