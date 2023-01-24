from lc_base_item import BaseItem

class CommonArmoryElement(BaseItem):
    def __init__(
        self,
        name,
        basePrice,
        armoryElementType,
        rarity,
        quality,
        defence,
        modificators
    ):
        #super().__init__(name, basePrice, f'armor_{armoryElementType}', rarity, quality, modificators)
        self.__name = name
        self.__basePrice = basePrice
        self.__itemType = f'armor_{armoryElementType}'
        self.__rarity = rarity
        self.__quality = itemQuality(quality)
        self.__modificators = modificators
        self.__defence = defence
        #self.__modificators = modificators

    def getDefence(self):
        return self.__defence

    #def getMods(self):
    #    return self.__modificators

class BattleBelt(BaseItem):
    def __init__(
        self,
        name,
        basePrice,
        #armoryElementType,
        rarity,
        quality,
        slots,
        modificators
    ):
        #super().__init__(name, basePrice, 'armor_battle_belt', rarity, quality, modificators)
        self.__name = name
        self.__basePrice = basePrice
        self.__itemType = 'armor_battle_belt'
        self.__rarity = rarity
        self.__quality = itemQuality(quality)
        self.__modificators = modificators
        #self.__defence = defence
        self.__beltInventory = [None for _ in range(slots)]
        self.__maxItems = slots
        #self.__modificators = modificators

    def getItem(self, number):
        if number >= self.__maxItems:
            return None
        else:
            return self.__beltInventory[number]

    def deleteItem(self, number):
        #? deleted item returning
        if number < self.__maxItems:
            self.__beltInventory[number] = None

    #? idk
    def deleteItemWithShift(self, number):
        pass

    def addItem(self, item):
        if self.__beltInventory.count(None) != 0:
        #if len(self.__beltInventory) < self.__maxItems:
            
            self.__beltInventory[self.__findNone()] = item #TODO stacking the same items

    def __findNone(self):
        for i in range(self.__beltInventory):
            if self.__beltInventory == None:
                return i

    
class Ring(BaseItem):
    def __init__(
        self,
        name,
        basePrice,
        rarity,
        quality,
        hand,
        finger,
        modificators
    ):
        #super().__init__(name, basePrice, f'armor_ring_{hand}_hand_{finger}_finger', rarity, quality, modificators)
        self.__name = name
        self.__basePrice = basePrice
        self.__itemType = f'armor_ring_{hand}_hand_{finger}_finger'
        self.__rarity = rarity
        self.__quality = itemQuality(quality)
        self.__modificators = modificators
        self.__hand = hand
        self.__finger = finger
        #self.__modificators = modificators

class Talisman(BaseItem):
    def __init__(
        self,
        name,
        basePrice,
        rarity,
        quality,
        modificators
    ):
        #super().__init__(name, basePrice, 'armor_talisman', rarity, quality, modificators)
        self.__name = name
        self.__basePrice = basePrice
        self.__itemType = 'armor_talisman'
        self.__rarity = rarity
        self.__quality = itemQuality(quality)
        self.__modificators = modificators
        #self.__modificators = modificators

class ForceField(BaseItem):
    def __init__(
        self,
        name,
        basePrice,
        armoryElementType,
        rarity,
        quality,
        capacity,
        durability, #! AKA FF's HP
        damageAbsorbationPercent,
        modificators
    ):
        #super().__init__(name, basePrice, f'armor_{armoryElementType}', rarity, quality, modificators)
        self.__name = name
        self.__basePrice = basePrice
        self.__itemType = 'armor_force_field'
        self.__rarity = rarity
        self.__quality = itemQuality(quality)
        self.__modificators = modificators
        self.__capacity = capacity
        self.__durability = durability
        self.__damageAbsorbationPercent = damageAbsorbationPercent
        #TODO Damage getting to the force field
        #self.__modificators = modificators