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
    # Fractal, Darkest, Champion, Unique

quialityLevels = [
    'bronze',
    'silver',
    'gold',
    'platinum',
    'diamond'
]
class itemQuality:
    def __init__(self, level):
        self.__stars = 5 if level % 5 == 0 else level % 5
        self.__qLevel = quialityLevels[level // 5]
    # 1 level = 5 stars; levels: bronze, silver, gold, platinum, diamond