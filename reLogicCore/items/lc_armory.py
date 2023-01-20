#from lc_armor_element import ArmorElement

class EquipmentCell:
    def __init__(self, equipmentType):
        self.__cellItem = None
        self.__equipmentType = equipmentType
        self.__hasTheItem = False

    def putOnItem(self, item):
        pass

    def takeOffItem(self):
        self.__cellItem = None
        self.__hasTheItem = False
        #? Maybe it also will return the active item