from lc_item_rarity_quality import itemQuality, itemRarity

class BaseItem:
    '''
    Represents a class of a base item
    It includes the base item's name, price, rarity, quality and stats modificators
    Important: some items may not have modificators, it depends on the <itemType>
    '''
    def __init__(
        self,
        name,
        basePrice,
        itemType,
        rarity: itemRarity,
        quality,
        modificators,  #! some items may not have them
        maxStacking
    ):
        self.__name = name
        self.__basePrice = basePrice
        self.__itemType = itemType
        self.__rarity = rarity
        self.__quality = itemQuality(quality)
        self.__modificators = modificators
        self.__maxStack = maxStacking
        
    def getName(self):
        #'''
        #Returns the item's name
        #'''
        return self.__name
    
    def getBasePrice(self):
        '''
        Returns the item's price
        '''
        return self.__basePrice

    def getItemType(self):
        '''
        Returns the item's type
        '''
        return self.__itemType

    def getRarity(self):
        '''
        Returns the item's rarity
        '''
        return self.__rarity

    def getQuality(self):
        '''
        Returns the item's quality
        '''
        return self.__quality.gerQualityLevel()

    def getMods(self):
        '''
        Returns the item's stats modificators
        '''
        return self.__modificators

    def getMaxStacking(self):
        return self.__maxStack
