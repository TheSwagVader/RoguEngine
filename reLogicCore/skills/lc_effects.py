#from abc import ABC

class BaseEffect:
    '''
    Represents a class of a base effect
    Contains only one field, duration of the effect
    '''
    def __init__(self, duration):
        self.__duration = duration

    def getDuration(self):
        return self.__duration

class EffectBled(BaseEffect):
    '''
    Represents a class of the effect 'Bled'.
    During it, the entity is losing its health, <damage>/turn for <duration> turns
    If also poisoned, the effect strenghtens
    '''
    def __init__(self, duration, damage):
        super().__init__(duration)
        self.__damage = damage

    def strengthen(self):
        pass

    def getDamage(self):
        return self.__damage

class EffectPoisoned(BaseEffect):
    '''
    Represents a class of the effect 'Poisoned'.
    During it, the entity is losing its health, <damage>/turn for <duration> turns
    If also bled, the effect strenghtens
    '''
    def __init__(self, duration, damage):
        super().__init__(duration)
        self.__damage = damage

    def strengthen(self):
        pass

    def getDamage(self):
        return self.__damage

class EffectStunned(BaseEffect):
    '''
    Represents a class of the effect 'Stunned'.
    During it, the entity is not avaliable to do any action (skips a turn)
    '''

class EffectRiposte(BaseEffect):
    '''
    Represents a class of the effect 'Riposte'.
    During it. if the entity was attaked, it will riposte using the defined <skill>
    '''
    def __init__(self, duration, skill):
        super().__init__(duration)
        self.__skill = skill

    def getSkill(self):
        return self.__skill

class EffectWeakened(BaseEffect):
    '''
    Represents a class of the effect 'Weakened'.
    During it, some characteristicts of the entity is reduced by <percent> for <duration> turns
    Reducable characteristics are:
    * Damage
    * Skills' heal value
    * Defence
    * Current HP level
    * Resistances for the effects excl. "Weakened", "Buff" and "Riposte"
    * May be more...
    '''
    def __init__(self, duration, percent):
        super().__init__(duration)
        self.__percent = percent

    def getPercent(self):
        return self.__percent

class EffectBuffed(BaseEffect):
    '''
    Represents a class of the effect "Buffed"
    During it, the entity's characteristics are increased for <duration> turns
    The increasable characteristics are written in <buffs> list
    '''
    def __init__(self, duration, buffs):
        super().__init__(duration)
        self.__buffs = buffs

    def getBuffs(self):
        return self.__buffs

class EffectDebuffed(BaseEffect):
    '''
    Represents a class of the effect "Debuffed"
    During it, the entity's characteristics are decreased for <duration> turns
    The decreasable characteristics are written in <debuffs> list
    '''
    def __init__(self, duration, debuffs):
        super().__init__(duration)
        self.__debuffs = debuffs

    def getDebuffs(self):
        return self.__debuffs