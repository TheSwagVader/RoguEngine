class Inventory:
    def __init__(self, slots):
        self.__inventory = [None for _ in range(slots)]
        self.__maxItems = slots
