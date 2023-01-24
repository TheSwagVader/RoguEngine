from lc_inventory_stack import Stack


class Inventory:
    def __init__(self, slots):
        self.__inventory = [Stack() for _ in range(slots)]
        self.__maxItems = slots

    #def getItem(self, number):
    #    if number >= self.__maxItems:
    #        return None
    #    else:
    #        return self.__inventory[number]
#
    #def deleteItem(self, number):
    #    #? deleted item returning
    #    if number < self.__maxItems:
    #        self.__inventory[number] = None
#
    def addItem(self, item):
        if self.__inventory.count(None) != 0:
        #if len(self.__inventory) < self.__maxItems:
            
            self.__inventory[self.__findNone()] = item #TODO stacking the same items
#
   # def __findNone(self):
   #     for i in range(self.__inventory):
   #         if self.__inventory == None:
   #             return i