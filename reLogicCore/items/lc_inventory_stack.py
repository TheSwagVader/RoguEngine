class Stack:
    def __init__(self):
        self.__item = None
        self.__amount = 0
        self.__maxAmount = 0
    
    def putItem(self, item):
        if self.__item == None:
            self.__item = item
            self.__amount = 1
            self.__maxAmount = item.getMaxStacking()

    def dropOne(self):
        if self.__amount > 1:
            self.__amount -= 1
            return self.__item
        elif self.__amount == 1:
            tmp = self.__item
            self.clear()
            return tmp
        else:
            pass #TODO exception if empty

    def dropEverything(self):
        tmp = [self.__item, self.__amount]
        self.clear()
        return tmp

    def clear(self):
        self.__item = None
        self.__amount = 0
        self.__maxAmount = 0

    def __nonEmpty(self):
        pass