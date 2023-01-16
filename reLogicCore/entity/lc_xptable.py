class XPTable:
    '''Defines the XP table for the character'''

    def __init__(self):
        self.__table = None
    
    def setXPTable(self, table):
        '''Sets the XP table with the list of integers'''
        self.__table = table
    
    def getRequirableXP(self, level):
        '''
        Returns a requirable value of XP for the level following the XP table
        '''