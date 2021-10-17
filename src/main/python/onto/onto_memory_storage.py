from src.main.python.onto.onto_storage import OntoStorageInterface


class OntoMemoryStorage(OntoStorageInterface):
    ontoChildParents = dict()
    ontoParentChildren = dict()
    ontoClassIdLabel = dict()

    def __init__(self):
        pass
    def insertClassIdLabelOnto(self, classId: str, label: str):
        self.ontoClassIdLabel[classId] = label
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

    def findParentsById(self, classId: str) -> tuple:
        return self.ontoChildParents.get(classId)

    def findChildren(self, parents: tuple) -> list:
        return self.ontoParentChildren.get(parents)