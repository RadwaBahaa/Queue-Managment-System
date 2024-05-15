class ParentQueue:
    _index = 0

    # Constructor which create a new queue
    def __init__(self):
        self.__queue = []

    # Insert method to get the queue
    def getdata(self):
        return self.__queue

    # Insert method to the queue
    def insertdata(self, value):
        self.__queue.append(value)
        self._index += 1

    # Instance method to pop from the queue
    def pop(self):
        if self.is_empty():
            raise IndexError('You try to pop from an empty Queue')
        return self.__queue.pop(0)

    # Instance method to Ask if the queue empty
    def is_empty(self):
        if len(self.__queue) == 0:
            return True
        else:
            return False
