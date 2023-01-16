import lc_sysconst

class CharacteristicBasis:
    '''
    This class defines the basis of character's stats for each player class
    '''
    def __init__(self):
        self.__chars = lc_sysconst.NULL_CHARS
        #self.__charsNames = lc_sysconst.CHARS_NAMES
    
    def setBasis(self, parameters):
        '''
        Sets the basis with the values in "parameters" list.
        The order of the parameters:
        * HP (Health)
        * AP (Action points)
        * MP (Mana points)
        * SP (Special points)
        * OD (Overdrive)
        * STR (Strength)
        * SPD (Speed)
        * INT (Intellegence)
        * DEF (Defence)
        * VIT (Vitality)
        * PROT (Protection)
        * DODGE
        * LUCK
        * RES (Resistance)
        * SEC (Secrecy)
        * POW (Power)
        '''

        for i in range(len(self.__charsNames)):
            self.__chars[lc_sysconst.CHARS_NAMES[i]] = parameters[i]
    
    def getBasisCharacteristic(self, name):
        '''
        Returns a wishful characteristic of the basis
        '''

        return self.__chars[name]