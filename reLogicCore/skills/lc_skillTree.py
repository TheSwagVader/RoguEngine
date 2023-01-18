from lc_skillTreeElement import SkillTreeElement

class SkillTree:
    def __init__(self):
        #self.__nodes = []
        #self.__skills = []
        self.__layers = []
    
    def __addEmptyLayer(self):
        self.__layers.append([])

    def addLeaf(self, skillTreeElement, layer):
        if layer < len(self.__layers):
            self.__addEmptyLayer()
        
        self.__layers[layer].append(skillTreeElement)

    def activateLeaf(self, layer, number):
        leaf = self.__layers[layer][number]
        leafConnections = leaf.getConnections()
        flag = True
        for leafConnection in leafConnections:
            if not self.__layers[layer-1][leafConnection].isActivated():
                flag = False
                break
        if flag:
            self.__layers[layer][number].activate()