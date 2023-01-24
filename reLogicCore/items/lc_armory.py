#from lc_armor_element import ArmorElement
import lc_it_sysconst
class EquipmentCell:
    def __init__(self, equipmentType):
        self.__cellItem = None
        self.__equipmentType = equipmentType
        self.__hasTheItem = False

    def putOnItem(self, item):
        if item.getItemType() != self.__equipmentType:
            pass #TODO exception if the cell has the item
        else:
            self.__cellItem = item
            self.__hasTheItem = True

    def takeOffItem(self):
        self.__cellItem = None
        self.__hasTheItem = False
        #? Maybe it also will return the active item

    def hasTheItem(self):
        return self.__hasTheItem

    def getEquipmentType(self):
        return self.__equipmentType

class CharacterEquipment:

    def __init__(self):
        self.__charEquipment = dict()
        for armorTypeElement in lc_it_sysconst.ARMOR_TYPES:
            self.__charEquipment[armorTypeElement] = EquipmentCell(armorTypeElement)

    def putOnItem(self, equipmentType, item):
        self.__charEquipment[equipmentType].putOnItem(item)

    def takeOffItem(self, equipmentType):
        self.__charEquipment[equipmentType].takeOffItem()

    def hasTheItem(self, equipmentType):
        return self.__charEquipment[equipmentType].hasTheItem()

    def getEquipmentType(self, equipmentType):
        return self.__charEquipment[equipmentType].getEquipmentType()

    def replaceItem(self, equipmentType, item):
        self.takeOffItem(equipmentType)
        self.putOnItem(equipmentType, item)