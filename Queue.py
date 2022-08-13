
class Queue():                          #FIFO - FIRST IN FIRST OUT
    def __init__(self) -> None:
        self.data = []
    def isEmpty(self):
        return self.data == []
    def enqueue(self,data):
        self.data.insert(0,data)
        return "The data is added to the queue {}".format(data)
    def dequeue(self):
        if self.isEmpty() == True:
            print("The queue has empty values sorry")
        else:
            d = self.data.pop()
            return "The value popped from the queue is {}".format(d)
    def len_(self):
        return "The length of the queue is {}".format(len(self.data))
    def lis(self):
        print("The entire queue is {}".format(self.data))


l = Queue()
l.lis()
print(l.isEmpty())
print(l.enqueue(2))
print(l.enqueue(3))
print(l.enqueue(4))
print(l.enqueue(5))
l.lis()
print(l.dequeue())
l.lis()
print(l.len_())
print(l.isEmpty())
