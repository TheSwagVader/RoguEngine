class BaseSkill:
    '''
    Represents a base skill class
    '''
    def __init__(self, name, cost):
        self.__name = name
        self.__cost = cost

    def getName(self):
        return self.__name
    
    def getCost(self):
        return self.__cost

class AttackSkill(BaseSkill): 
    def __init__(self, name, cost, damage, crit, accurancy, effects):
        super().__init__(name, cost)
        self.__damage = damage
        self.__crit = crit
        self.__accurancy = accurancy
        self.__effects = effects

class SupportSkill(BaseSkill): ...

class CombinedSkill(BaseSkill): ...   