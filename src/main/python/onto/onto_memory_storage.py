from onto_storage import OntoStorageInterface


# Class which handle storage in memory using dictionnary
class OntoMemoryStorage(OntoStorageInterface):
    # Associate onto classId and a tuple of parents
    __onto_child_parents = dict()

    # Associate tuple of parents and list of children
    __onto_parent_children = dict()

    # Associate onto classId and label
    __onto_class_id_label = dict()

    # Associate onto label and classId
    __onto_label_class_id = dict()

    def __init__(self):
        pass

    def insertClassIdLabelOnto(self, classId: str, label: str):
        self.__onto_class_id_label[classId] = label
        pass

    def insertLabelClassIdOnto(self, classId: str, label: str):
        self.__onto_label_class_id[label] = classId
        pass

    def insertClassIdParentsOnto(self, classId: str, parents: tuple):
        self.__onto_child_parents[classId] = parents
        pass

    def addChildToParents(self, tupleParents: tuple, idChild: str):
        if self.__onto_parent_children.get(tupleParents) is None:
            self.__onto_parent_children[tupleParents] = []
        id: list = self.__onto_parent_children[tupleParents]
        id.append(idChild)
        pass

    def findLabelById(self, classId: str) -> str:
        return self.__onto_class_id_label.get(classId)

    # Find classId from label
    def findClassIdByLabel(self, label: str) -> str:
        return self.__onto_label_class_id.get(label)

    def findParentsById(self, classId: str) -> tuple:
        return self.__onto_child_parents.get(classId)

    def findChildren(self, parents: tuple) -> list:
        return self.__onto_parent_children.get(parents)
