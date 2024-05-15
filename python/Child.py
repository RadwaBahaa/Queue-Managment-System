from Parent import ParentQueue
from tabulate import tabulate
import json

class QueueOutOfRangeException(Exception):
    pass

class ChildQueue(ParentQueue):
    __alldata = []

    # Constructor which create a new queue
    def __init__(self, name, size):
        self.__queuesinfo = {}
        try:
            super().__init__()
            self.__maxsize = int(size)
        except ValueError:
            raise ValueError('Queue maxsize must be an integer')
        else:
            if self.__maxsize < 0:
                raise ValueError('Queue maxsize must be a positive integer')
            elif self.__maxsize == 0:
                raise ValueError('Queue maxsize cannot be zero')
            if self.searchqueue(name):
                raise Exception('The Queue is exist')

            self.__queuesinfo['Name'] = name
            self.__queuesinfo['Queue'] = ParentQueue.getdata(self)

            self.__alldata.append(self.__queuesinfo)
            self.save()

    # Insert method to insert data to the queue
    def insert(self, value):
        if self._index >= self.__maxsize:
            raise QueueOutOfRangeException("Queue is full")
        ParentQueue.insertdata(self, value)
        self.save()

    def update(self, name):
        for data in self.__alldata:
            if data['Name'] == name:
                data['Queue'] = ParentQueue.getdata(self)
                self.save()

    # Insert method to get data fo a specific queue
    def getqueue(self, name):
        for data in self.__alldata:
            if self.searchqueue(name):
                return f'The Queue name is: {data['Name']} \nthe Queue is: {data["Queue"]}'
            else:
                return 'The Queue is not exist'

    # Insert method to delete a specific queue
    def deletequeue(self, name):
        for data in self.__alldata:
            if self.searchqueue(name):
                self.__alldata.remove(data)
                self.save()
            else:
                raise Exception('The Queue is not exist')

    # Insert method to delete all queues
    def deleteallqueues(self):
        for data in self.__alldata:
            self.__alldata.remove(data)
        return '_____ The Queue is empty now _____'

    @classmethod
    def searchqueue(cls, name):
        for value in cls.__alldata:
            if value['Name'] == name:
                return True
            else:
                return False

    @classmethod
    def empty(cls):
        if len(cls.__alldata) == 0:
            raise Exception('There is no data')

    @classmethod
    def save(cls):
        file = open('package.json', 'w')
        json.dump(cls.__alldata, file, indent=2)
        file.close()
        print('____The file has been saved Successfully!____')

    @classmethod
    def load(cls):
        if cls.__alldata:
            file = open('package.json', 'r')
            cls.__alldata = json.load(file)
            return tabulate(cls.__alldata)
        else:
            raise Exception('There is no data in the package')
