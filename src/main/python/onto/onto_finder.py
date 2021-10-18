from onto_storage import OntoStorageInterface

#This class has responsability to find onto from id or label
class OntoFinder:
    __ontoStorage:OntoStorageInterface

    def __init__(self,ontoStorage: OntoStorageInterface):
        self.ontoStorage = ontoStorage

    #Find onto from class id
    def searchEntityById(self,classId):
        ontoClassIdLabelDeep = dict()
        self.__searchEntityByIdAndDeep((classId,), 0, ontoClassIdLabelDeep,False)
        ontoLabelDeep = self.__ontoIdClassLabelDeepToOntoLabelDeep(ontoClassIdLabelDeep)
        return ontoLabelDeep

    def __ontoIdClassLabelDeepToOntoLabelDeep(self,ontoClassIdLabelDeep: dict):
        ontoLabelDeep = dict()
        values = ontoClassIdLabelDeep.values()
        for value in values:
            label = value[0]
            deep = value[1]
            ontoLabelDeep[label] = deep
        return ontoLabelDeep

    def __isOntoProcessed(self,classId, ontoClassIdLabelDeep):
        return ontoClassIdLabelDeep.get(classId) is None

    def __searchEntityByIdAndDeep(self,classIds: tuple, deep, ontoClassIdLabelDeep, childProcessing:bool):
        deepParent = deep + 1
        deepChild = deep - 1
        for classId in classIds:
            print(classId)
            label = self.ontoStorage.findLabelById(classId)
            if label is not None and len(label) > 0:
                if self.__isOntoProcessed(classId, ontoClassIdLabelDeep):
                    ontoClassIdLabelDeep[classId] = (label, deep,)
                    if not childProcessing:
                        parents = self.ontoStorage.findParentsById(classId)
                        if parents is not None and len(parents) > 0:
                            self.__searchEntityByIdAndDeep(parents, deepParent, ontoClassIdLabelDeep,False)
        if deepChild >= 0:
            children = self.ontoStorage.findChildren(classIds)
            if children is not None and len(children) > 0:
                self.__searchEntityByIdAndDeep(tuple(children), deepChild, ontoClassIdLabelDeep,True)