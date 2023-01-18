class Buff:
    def __init__(self, characteristic, buffType, buffValue):
        '''
        Represents a class of a buff, that increases the entity's characteristics
        Buff types:
        + - increases for <buffValue> points
        % - increases for <buffValue> percent
        '''
        self.__characteristic = characteristic
        self.__buffType = buffType
        self.__buffValue = buffValue
    
    def getBuffTuple(self):
        return (
            self.__characteristic,
            self.__buffType,
            self.__buffValue
        )