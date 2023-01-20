from lc_base_item import BaseItem

class Weapon(BaseItem):
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
        super().__init__(name, basePrice, f'weapon_{weaponType}', rarity, quality)
        self.__damageRange = damageRange
        self.__baseCritChance = baseCriticalChance
        self.__handsRequired = handsRequired
        self.__modificatios = modificators
        self.__skillset = skillset
        self.__assignedSkillsValue = len(skillset)
    
    def getMods(self):
        return self.__modificatios

    def getWeaponSkill(self, number):
        if number >= self.__assignedSkillsValue:
            return None
        else:
            return self.__skillset[number]

    def getBaseStats(self):
        return (self.__damageRange, self.__baseCritChance)

    def getRequiredHandsValue(self):
        return self.__handsRequired