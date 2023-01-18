class SkillTreeElement:
    def __init__(self, skill, charRequirements, connections):
        self.__skill = skill
        self.__charRequirements = charRequirements
        self.__isActivated = False
        self.__connections = connections

    def getSkill(self):
        return self.__skill
    
    def getCharRequirements(self):
        return self.__charRequirements

    def getConnections(self):
        return self.__connections

    def isActivated(self):
        return self.__isActivated

    def activate(self):
        self.__isActivated = True
    
    def deactivate(self):
        self.__isActivated = False