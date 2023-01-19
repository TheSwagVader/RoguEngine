from lc_item_rarity_quality import itemQuality, itemRarity

class BaseItem:
    def __init__(self, name, basePrice, itemType, rarity: itemRarity, quality):
        self.__name = name
        self.__basePrice = basePrice
        self.__itemType = itemType
        self.__rarity = rarity
        self.__quality = itemQuality(quality)
        
    def getName(self):
        return self.__name
    
    def getBasePrice(self):
        return self.__basePrice

    def getItemType(self):
        return self.__itemType

    def getRarity(self):
        return self.__rarity

    def getQuality(self):
        return self.__quality.gerQualityLevel()

