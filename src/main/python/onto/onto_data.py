class EntityData:
    __classId: str
    __label: str
    __parents: tuple

    def __init__(self,classId, label, parents):
        self.__classId = classId
        self.__label = label
        self.__parents = parents

    def getClassId(self):
        return self.__classId

    def getLabel(self):
        return self.__label

    def getParents(self):
        return self.__parents