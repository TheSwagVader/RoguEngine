from lc_base_item import BaseItem

class Weapon(BaseItem):
    '''
    '''
    def __init__(
        self,
        name,
        basePrice,
        weaponType,
        rarity,
        quality,
        damageRange,
        baseCriticalChance,
        handsRequired,
        modificators,
        skillset

    ):
        #super().__init__(name, basePrice, f'weapon_{weaponType}', rarity, quality, modificators)
        self.__name = name
        self.__basePrice = basePrice
        self.__itemType = f'weapon_{weaponType}'
        self.__rarity = rarity
        self.__quality = itemQuality(quality)
        self.__modificators = modificators
        self.__damageRange = damageRange
        self.__baseCritChance = baseCriticalChance
        self.__handsRequired = handsRequired
        self.__modificators = modificators
        self.__skillset = skillset
        self.__assignedSkillsValue = len(skillset)
    
    #def getMods(self):
    #    return self.__modificators

    def getWeaponSkill(self, number):
        if number >= self.__assignedSkillsValue:
            return None
        else:
            return self.__skillset[number]

    def getBaseStats(self):
        return (self.__damageRange, self.__baseCritChance)

    def getRequiredHandsValue(self):
        return self.__handsRequired