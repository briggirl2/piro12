class stack:

    def __init__(self):
        self.__arr = []
        self.__top = 0

    def push(self, item):
        self.__arr.append(item)
        self.__top += 1

    def isEmpty(self):
        return self.__arr == []

    def pop(self):
        if self.isEmpty():
            return False
        self.__top -= 1
        item = self.__arr[self.__top]
        del(self.__arr[self.__top])
        return item

    def pick(self):
        if self.isEmpty():
            return False
        item = self.__arr[self.__top - 1]
        return item
