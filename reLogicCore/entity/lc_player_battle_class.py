import lc_sysconst

class PlayerBattleClass:
    '''
    This class defines a class of player's character.
    The class influences limits for the equipment that player can use,
    player's skills and start characteristics 
    '''

    def __init__(self, name):
        self.__name = name
        self.__charsInfluence = lc_sysconst.NULL_CHARS

    def setCharacteristicInfluence(self, inf_params):
        '''
        Sets the inflience with the values in "inf_params" list.
        It uses a tuple with the following structure: (characteristicName, influenceType)

        Influence types:
        * A - Addition
        * M - Multiplication
        * D - Division

        The order of the parameters:
        * HP (Health)
        * AP (Action points)
        * MP (Mana points)
        * SP (Special points)
        * OD (Overdrive)
        * STR (Strength)
        * SPD (Speed)
        * INT (Intellegence)
        * ACC (Accurancy)
        * CRIT (Base critical change)
        * VIT (Vitality)
        * PROT (Protection)
        * DODGE
        * LUCK
        * RES (Resistance)
        * SEC (Secrecy)
        * POW (Power)
        '''

        for i in range(len(lc_sysconst.CHARS_NAMES)):
            self.__charsInfluence[lc_sysconst.CHARS_NAMES[i]] = parameters[i]
    
    def getInfluence(self, name):
        '''
        Returns a wishful characteristic of the influence table
        '''

        return self.__charsInfluence[name]

    def getName(self):
        '''
        Returns tha class' name
        '''
        return self.__name  
        