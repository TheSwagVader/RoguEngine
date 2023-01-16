from lc_entity import Entity
class Player(Entity):
    def __init__(self, health, role, mana):
        Entity.__init__(health, role)
        self.mana = mana