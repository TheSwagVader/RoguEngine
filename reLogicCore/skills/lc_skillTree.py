#from lc_skillTreeElement import SkillTreeElement
from lc_sk_sysexceptions import InvalidLayerNumber

class SkillTreeLeaf:
    '''
    Represtnts the class af a skill tree leaf, that contains the skill, its requirements and nodes
    Nodes are the skills' numbers on the previous layer in the skill tree that must be activated to activate this leaf
    Nodes are included in the list of integers <nodes>
    TODO: more requirements such as character's stats and so on
    '''
    def __init__(self, skill, reqLevel, nodes):
        self.__skill = skill
        self.__reqLevel = reqLevel
        self.__reqLevelPassed = False
        self.__isActivated = False
        self.__nodes = nodes

    def getSkill(self):
        '''
        Returns the leaf's skill
        '''
        return self.__skill

    def getReqLevel(self):
        '''
        Returns the leaf's level requirement to activate
        '''
        return self.__reqLevel

    def getNodes(self):
        '''
        Returns the leaf's nodes
        '''
        return self.__nodes

    def isActivated(self):
        '''
        Returns the leaf's status of activation
        It's needed for the skill tree
        '''
        return self.__isActivated

    def checkLevelRequirement(self, level):
        '''
        Sets the leaf's status of level requirement passing, if <level> >= <reqLevel>
        '''
        if level >= self.__reqLevel:
            self.__reqLevelPassed = True
    
    def isReqPassedByLevel(self):
        '''
        Returns the leaf's status of level requirement passing
        It's needed for the skill tree
        '''
        return self.__reqLevelPassed

    def activate(self):
        '''
        Activates the leaf if the requirements are passed
        '''
        if self.isReqPassedByLevel():
            self.__isActivated = True
    
    def deactivate(self):
        '''
        Deactivates the leaf
        '''
        self.__isActivated = False

class SkillTree:
    '''
    Represents a class of a skill tree
    It contains layers in which the leaves are inserted
    ''' 
    def __init__(self):
        self.__layers = []
    
    def __addEmptyLayer(self):
        self.__layers.append([])

    def addLeaf(self, skillTreeLeaf, layer):
        '''
        Adds a skill tree leaf to the tree
        <layer> must be less than or equal to current numbers of skill tree layers
        ''' 
        if layer == len(self.__layers):
            self.__addEmptyLayer()
        elif layer > len(self.__layers):
            raise InvalidLayerNumber(
                'The leaf must be inserted into a layer with number <= %d, got %d' 
                % (len(self.__layers), layer)
                )
        
        self.__layers[layer].append(skillTreeLeaf)

    def isLeafReqPassed(self, layer, number):
        '''
        Returns the status of the skill tree leaf's of level requirement passing
        '''
        return self.__layers[layer][number].isReqPassedByLevel()

    def isLeafActivated(self, layer, number):
        '''
        Returns the status of the skill tree leaf's of activation
        '''
        return self.__layers[layer][number].isActivated()

    def getLeafNodes(self, layer, number):
        '''
        Returns the nodes of the skill tree leaf
        '''
        return self.__layers[layer][number].getNodes()
    
    def checkLeafLevelRequirement(self, layer, number, level):
        '''
        Sets the status of the skill tree leaf's of level requirement passing, if <level> >= <reqLevel>
        '''
        self.__layers[layer][number].checkLevelRequirement(level)

    def activateLeaf(self, layer, number):
        '''
        Activates the leaf if all the requirements are passed and
        all the skills in nodes are activated
        '''
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