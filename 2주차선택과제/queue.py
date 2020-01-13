class queue:
    def __init__(self):
        self.__arr = []
        self.__front = 0
        self.__rear = 0

    def push(self, item):
        self.__arr.append(item)
        self.__rear += 1

    def isEmpty(self):
        if self.__front >= self.__rear:
            return True
        return False

    def pop(self):
        if self.isEmpty():
            return False
        item = self.__arr[self.__front]
        del(self.__arr[self.__front])
        self.__rear -= 1
        return item

    def peek(self):
        if self.isEmpty():
            return False
        return self.__arr[self.__front]
#
#
# q = queue()
# q.push(1)
# print(q.peek())
# q.push(2)
# print(q.peek())
# print(q.pop())
# print(q.peek())
# print(q.pop())
# print(q.peek())
# print(q.isEmpty())
# q.push(3)
# print(q.isEmpty())
# print(q.peek())


