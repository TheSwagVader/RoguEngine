from enum import Enum

class itemRarity(Enum):
    Trash,
    Common,
    Uncommon,
    Rare,
    VeryRare,
    SuperRare,
    Epic,
    Legendary,
    Mythic,
    Divine,
    Eldritch,
    Fractal,
    Darkest,
    Champion,
    Unique = range(15)
    #Trash, Common, Uncommon, Rare, Very rare, Super rare, Epic, Legendary, Mythic, Divine, Eldritch
    # Fractal, Darkest, Champion, Unique; May be more


ITEM_QUALITY_LEVELS = [
    'bronze',
    'silver',
    'gold',
    'platinum',
    'diamond'
]
class itemQuality:
    def __init__(self, level):
        self.__stars = 5 if level % 5 == 0 else level % 5
        self.__qLevel = level // 5
        self.__qLevelName = ITEM_QUALITY_LEVELS[level // 5]

    #def getStars(self):
    #    return self.__stars
    
    def gerQualityLevel(self):
        return (self.__qLevelName, self.__stars)
    
    def raiseQuality(self):
        self.__stars += 1
        if self.__stars > 5:
            self.__stars = 1
            if self.__qLevel < 4:
                self.__qLevel += 1
                self.__qLevelName = ITEM_QUALITY_LEVELS[self.__qLevel]
    # 1 level = 5 stars; levels: bronze, silver, gold, platinum, diamond