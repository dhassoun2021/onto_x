from onto_storage import OntoStorageInterface

# Class which handle storage in memory using dictionnary
class OntoMemoryStorage(OntoStorageInterface):

    # Associate onto classId and a tuple of parents
    ontoChildParents = dict()

    # Associate tuple of parents and list of children
    ontoParentChildren = dict()

    # Associate onto classId and label
    ontoClassIdLabel = dict()

    # Associate onto label and classId
    ontoLabelClassId = dict()

    def __init__(self):
        pass
    def insertClassIdLabelOnto(self, classId: str, label: str):
        self.ontoClassIdLabel[classId] = label
        pass

    def insertLabelClassIdOnto(self, classId: str, label: str):
        self.ontoLabelClassId[label] = classId
        pass
    def insertClassIdParentsOnto(self, classId: str, parents: tuple):
        self.ontoChildParents[classId] = parents
        pass

    def addChildToParents(self, tupleParents: tuple, idChild: str):
        if self.ontoParentChildren.get(tupleParents) is None:
            self.ontoParentChildren[tupleParents] = []
        id: list = self.ontoParentChildren[tupleParents]
        id.append(idChild)
        pass

    def findLabelById(self, classId: str) -> str:
        return self.ontoClassIdLabel.get(classId)

    # Find classId from label
    def findClassIdByLabel(self, label: str) -> str:
        return self.ontoLabelClassId.get(label)

    def findParentsById(self, classId: str) -> tuple:
        return self.ontoChildParents.get(classId)

    def findChildren(self, parents: tuple) -> list:
        return self.ontoParentChildren.get(parents)