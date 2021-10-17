from src.main.python.onto.onto_storage import OntoStorageInterface


class OntoFinder:
    ontoStorage:OntoStorageInterface

    def __init__(self,ontoStorage: OntoStorageInterface):
        self.ontoStorage = ontoStorage

    def searchEntityById(self,classId):
        ontoClassIdLabelDeep = dict()
        self.searchEntityByIdAndDeep((classId,), 0, ontoClassIdLabelDeep)
        ontoLabelDeep = self.ontoIdClassLabelDeepToOntoLabelDeep(ontoClassIdLabelDeep)
        return ontoLabelDeep

    def ontoIdClassLabelDeepToOntoLabelDeep(self,ontoClassIdLabelDeep: dict):
        ontoLabelDeep = dict()
        values = ontoClassIdLabelDeep.values()
        for value in values:
            label = value[0]
            deep = value[1]
            ontoLabelDeep[label] = deep
        return ontoLabelDeep

    def isOntoProcessed(self,classId, ontoClassIdLabelDeep):
        return ontoClassIdLabelDeep.get(classId) is None

    def searchEntityByIdAndDeep(self,classIds: tuple, deep, ontoClassIdLabelDeep):
        deepParent = deep + 1
        deepChild = deep - 1
        for classId in classIds:
            label = self.ontoStorage.findLabelById(classId)
            if label is not None and len(label) > 0:
                if self.isOntoProcessed(classId, ontoClassIdLabelDeep):
                    ontoClassIdLabelDeep[classId] = (label, deep,)
                    parents = self.ontoStorage.findParentsById(classId)
                    if parents is not None and len(parents) > 0:
                        self.searchEntityByIdAndDeep(parents, deepParent, ontoClassIdLabelDeep)
        if deepChild >= 0:
            children = self.ontoStorage.findChildrenById(classIds)
            if children is not None and len(children) > 0:
                self.searchEntityByIdAndDeep(tuple(children), deepChild, ontoClassIdLabelDeep)