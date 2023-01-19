#from lc_skillTreeElement import SkillTreeElement
from lc_sk_sysexceptions import InvalidLayerNumber

class SkillTreeLeaf:
    def __init__(self, skill, reqLevel, nodes):
        self.__skill = skill
        self.__reqLevel = reqLevel
        self.__reqLevelPassed = False
        self.__isActivated = False
        self.__nodes = nodes

    def getSkill(self):
        return self.__skill

    def getReqLevel(self):
        return self.__reqLevel

    def getNodes(self):
        return self.__nodes

    def isActivated(self):
        return self.__isActivated

    def checkLevelRequirement(self, level):
        if level >= self.__reqLevel:
            self.__reqLevelPassed = True
    
    def isReqPassedByLevel(self):
        return self.__reqLevelPassed

    def activate(self):
        self.__isActivated = True
    
    def deactivate(self):
        self.__isActivated = False

class SkillTree:
    def __init__(self):
        self.__layers = []
    
    def __addEmptyLayer(self):
        self.__layers.append([])

    def addLeaf(self, skillTreeLeaf, layer):
        if layer == len(self.__layers):
            self.__addEmptyLayer()
        elif layer > len(self.__layers):
            raise InvalidLayerNumber(
                'The leaf must be insetred into a layer with number <= %d, got %d' 
                % (len(self.__layers), layer)
                )
        
        self.__layers[layer].append(skillTreeLeaf)

    def isLeafReqPassed(self, layer, number):
        return self.__layers[layer][number].isReqPassedByLevel()

    def isLeafActivated(self, layer, number):
        return self.__layers[layer][number].isActivated()

    def getLeafNodes(self, layer, number):
        return self.__layers[layer][number].getNodes()
    
    def checkLeafLevelRequirement(self, layer, number, level):
        self.__layers[layer][number].checkLevelRequirement(level)

    def activateLeaf(self, layer, number):
        if self.isLeafReqPassed(layer, number):
            leafNodes = self.getLeafNodes(layer, number)
            if len(leafNodes) != 0:
                flag = True
                for leafNode in leafNodes:
                    if not self.isLeafActivated(layer-1, leafNode):
                        flag = False
                        break
                if flag:
                    self.__layers[layer][number].activate()
            else:
                self.__layers[layer][number].activate()