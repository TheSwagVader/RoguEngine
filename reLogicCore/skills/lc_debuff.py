class Debuff:
    def __init__(self, characteristic, debuffType, debuffValue):
        '''
        Represents a class of a debuff, that decreases the entity's characteristics
        Debuff types:
        - - decreases for <debuffValue> points
        % - decreases for <debuffValue> percent
        '''
        self.__characteristic = characteristic
        self.__dedebuffType = debuffType
        self.__debuffValue = debuffValue
    
    def getDebuffTuple(self):
        return (
            self.__characteristic,
            self.__debuffType,
            self.__debuffValue
        )