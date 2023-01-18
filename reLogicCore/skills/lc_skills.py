class BaseSkill:
    '''
    Represents a base skill class
    '''
    def __init__(self, name, cost):
        self.__name = name
        self.__cost = cost
    #    self.__type = 'base'

    def getName(self):
        return self.__name
    
    def getCost(self):
        return self.__cost

    #def getType(self):
    #    return self.__type

class AttackSkill(BaseSkill): 
    def __init__(self, name, cost, damage, crit, accuracy, effects):
        super().__init__(name, cost)
        self.__damage = damage
        self.__crit = crit
        self.__accuracy = accuracy
        self.__effects = effects

class SupportBuffSkill(BaseSkill):
    def __init__(self, name, cost, buffEffect):
        super().__init__(name, cost)
        self.__buffEffect = buffEffect

class SupportHealSkill(BaseSkill):
    def __init__(self, name, cost, healValue, crit):
        super().__init__(name, cost)
        self.__healValue = healValue
        self.__crit = crit

class SupportCombinedSkill(BaseSkill):
    def __init__(self, name, cost, buffEffect, healValue, crit):
        super().__init__(name, cost)
        self.__buffEffect = buffEffect
        self.__healValue = healValue
        self.__crit = crit

#class SupportSkill(BaseSkill):
#    def __init__(self, name, cost, supportType, values, crit):
#        super().__init__(name, cost)
#        self.__supportType = supportType
#        self.__values = values
#        self.__crit = crit

class CombinedSkill(BaseSkill):
    def __init__(
        self,
        name,
        cost,
        atkDamage,
        atkCrit,
        atkAccuracy,
        atkEffects, 
        supportSkillType,
        supportSkillParameters
    ):
        super().__init__(name, cost)
        #self.__attack = 0
        self.__atkDamage = atkDamage
        self.__atkCrit = atkCrit
        self.__atkAccuracy = atkAccuracy
        self.__atkEffects = atkEffects

        #self.__support = 0
        self.__supType = supportSkillType
        self.__supHealValue = None
        self.__supCrit = None
        self.__supBuffEffect = None

        if self.__supType == 'HEAL':
            self.__supHealValue = supportSkillParameters['healValue']
            self.__supCrit = supportSkillParameters['crit']
        elif self.__supType == 'BUFF':
            self.__supBuffEffect = supportSkillParameters['buffEffect']
        elif self.__supType == 'COMBO':
            self.__supBuffEffect = supportSkillParameters['buffEffect']
            self.__supHealValue = supportSkillParameters['healValue']
            self.__supCrit = supportSkillParameters['crit']
