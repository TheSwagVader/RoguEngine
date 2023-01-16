class BaseEffect:
    def __init__(self, duration):
        self.__duration = duration

    def getDuration(self):
        return self.__duration

class EffectBled(BaseEffect):
    def __init__(self, duration, damage):
        super().__init__(duration)
        self.__damage = damage

    def strengthen(self):
        pass

    def getDamage(self):
        return self.__damage

class EffectPoisoned(BaseEffect):
    def __init__(self, duration, damage):
        super().__init__(duration)
        self.__damage = damage

    def strengthen(self):
        pass

    def getDamage(self):
        return self.__damage

class EffectStunned(BaseEffect): ...

class EffectRiposte(BaseEffect):
    def __init__(self, duration, skill):
        super().__init__(duration)
        self.__skill = skill

    def getSkill(self):
        return self.__skill

class EffectWeakened(BaseEffect): 
    def __init__(self, duration, percent):
        super().__init__(duration)
        self.__percent = percent

    def getPercent(self):
        return self.__percent

class EffectBuffed(BaseEffect): 
    def __init__(self, duration, buffs):
        super().__init__(duration)
        self.__buffs = buffs

    def getBuffs(self):
        return self.__buffs

class EffectDebuffed(BaseEffect): 
    def __init__(self, duration, debuffs):
        super().__init__(duration)
        self.__debuffs = debuffs

    def getDebuffs(self):
        return self.__debuffs