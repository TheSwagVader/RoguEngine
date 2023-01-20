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
        super().__init__(name, basePrice, f'armor_{armoryElementType}', rarity, quality, modificators)
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
        super().__init__(name, basePrice, 'armor_battle_belt', rarity, quality, modificators)
        #self.__defence = defence
        self.__beltInventory = []
        self.__maxItems = slots
        #self.__modificators = modificators

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
        super().__init__(name, basePrice, f'armor_ring_{hand}_hand_{finger}_finger', rarity, quality, modificators)
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
        super().__init__(name, basePrice, 'armor_talisman', rarity, quality, modificators)
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
        super().__init__(name, basePrice, f'armor_{armoryElementType}', rarity, quality, modificators)
        self.__capacity = capacity
        self.__durability = durability
        self.__damageAbsorbationPercent = damageAbsorbationPercent
        #self.__modificators = modificators