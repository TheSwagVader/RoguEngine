from abc import abstractmethod

class BaseSkill:
    '''
    Represents a base skill class
    This class is abstract
    '''
    def __init__(self, name, cost):
        self.__name = name
        self.__cost = cost
    #    self.__type = 'base'

    def getName(self):
        return self.__name
    
    def getCost(self):
        return self.__cost

    @abstractmethod
    def getPrimalUsageList(self):
        pass

    #def getType(self):
    #    return self.__type

class AttackSkill(BaseSkill): 
    def __init__(self, name, cost, damage, crit, accuracy, effects):
        #super().__init__(name, cost)
        self.__name = name
        self.__cost = cost
        self.__damage = damage
        self.__crit = crit
        self.__accuracy = accuracy
        self.__effects = effects
    
    def getPrimalUsageList(self):
        return [
            [
                self.__name,
                self.__cost
            ],
            [
                self.__damage,
                self.__crit,
                self.__accuracy,
                self.__effects
            ]
        ]
        

class SupportBuffSkill(BaseSkill):
    def __init__(self, name, cost, buffEffect):
        #super().__init__(name, cost)
        self.__name = name
        self.__cost = cost
        self.__buffEffect = buffEffect
    
    def getPrimalUsageList(self):
        return [
            [
                self.__name,
                self.__cost
            ],
            [
                self.__buffEffect
            ]
        ]

class SupportHealSkill(BaseSkill):
    def __init__(self, name, cost, healValue, crit):
        #super().__init__(name, cost)
        self.__name = name
        self.__cost = cost
        self.__healValue = healValue
        self.__crit = crit
    
    def getPrimalUsageList(self):
        return [
            [
                self.__name,
                self.__cost
            ],
            [
                self.__healValue,
                self.__crit,
            ]
        ]

class SupportCombinedSkill(BaseSkill):
    def __init__(self, name, cost, buffEffect, healValue, crit):
        #super().__init__(name, cost)
        self.__name = name
        self.__cost = cost
        self.__buffEffect = buffEffect
        self.__healValue = healValue
        self.__crit = crit

    def getPrimalUsageList(self):
        return [
            [
                self.__name,
                self.__cost
            ],
            [
                self.__healValue,
                self.__crit,
                self.__buffEffect,
            ]
        ]

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
        #super().__init__(name, cost)
        self.__name = name
        self.__cost = cost
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

        #? Maybe redo for processing a tuple, not a dict
        if self.__supType == 'HEAL':
            self.__supHealValue = supportSkillParameters['healValue']
            self.__supCrit = supportSkillParameters['crit']
        elif self.__supType == 'BUFF':
            self.__supBuffEffect = supportSkillParameters['buffEffect']
        elif self.__supType == 'COMBO':
            self.__supBuffEffect = supportSkillParameters['buffEffect']
            self.__supHealValue = supportSkillParameters['healValue']
            self.__supCrit = supportSkillParameters['crit']

    def getPrimalUsageList(self):
        pul = [
            [
                self.__name,
                self.__cost
            ],
            [
                self.__atkDamage,
                self.__atkCrit,
                self.__atkAccuracy,
                self.__atkEffects
            ]
        ]
        if self.__supType == 'HEAL':
            pul[1].append(self.__supHealValue)
            pul[1].append(self.__supCrit)
        elif self.__supType == 'BUFF':
            pul[1].append(self.__supBuffEffect)
        elif self.__supType == 'COMBO':
            pul[1].append(self.__supHealValue)
            pul[1].append(self.__supCrit)
            pul[1].append(self.__supBuffEffect)

        return pul
