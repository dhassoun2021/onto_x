from onto_storage import OntoStorageInterface


# This class has responsability to find entity from class id or label
class OntoFinder:
    __ontoStorage: OntoStorageInterface

    def __init__(self, ontoStorage: OntoStorageInterface):
        self.ontoStorage = ontoStorage

    # Find entities hierarchies from class id
    # Return result hierarchy as dictionary as (classId,label) -> deep
    def search_entity_by_id(self, class_id):
        ontoClassIdLabelDeep = dict()
        self.__searchEntityByIdAndDeep((class_id,), 0, ontoClassIdLabelDeep, False)
        onto_result = self.__ontoIdClassLabelDeepToOntoResult(ontoClassIdLabelDeep)
        return onto_result

    # Find entities hierarchies from from label
    # Return result hierarchy as dictionary as (classId,label) -> depth
    def search_entity_by_label(self, label: str):
        classId = self.ontoStorage.findClassIdByLabel(label.upper())
        if classId is None or len(classId) == 0:
            return dict()
        return self.search_entity_by_id(classId)

    def __ontoIdClassLabelDeepToOntoResult(self, ontoClassIdLabelDeep: dict):
        onto_result = dict()
        keys = ontoClassIdLabelDeep.keys()
        for key in keys:
            tupleLabelDeep = ontoClassIdLabelDeep[key]
            onto_result[(key,tupleLabelDeep[0])] = tupleLabelDeep[1]
        return onto_result

    def __isEntityProcessed(self, classId, ontoClassIdLabelDeep):
        return ontoClassIdLabelDeep.get(classId) is None

    def __isParentsExist (self, parents: tuple):
        return parents is not None and len(parents) > 0

    def __isChildrenExist (self, children: list):
        return children is not None and len(children) > 0

    def __isEntityExist (self, label: str):
        return label is not None and len(label) > 0

    def __searchParents (self, classId: str, deepLevel: int, ontoClassIdLabelDeep: dict):
        parents = self.ontoStorage.findParentsById(classId)
        if self.__isParentsExist(parents):
            self.__searchEntityByIdAndDeep(parents, deepLevel, ontoClassIdLabelDeep, False)

    def __searchChildren (self, tuple_class_id: tuple, deepLevel: int, ontoClassIdLabelDeep: dict):
        children = self.ontoStorage.findChildren(tuple_class_id)
        if self.__isChildrenExist(children):
            self.__searchEntityByIdAndDeep(tuple(children), deepLevel, ontoClassIdLabelDeep, True)

    def __addEntity(self, class_id: str, ontoClassIdLabelDeep: dict, deep: int):
        label = self.ontoStorage.findLabelById(class_id)
        if self.__isEntityExist(label):
            if self.__isEntityProcessed(class_id, ontoClassIdLabelDeep):
                ontoClassIdLabelDeep[class_id] = (label, deep,)

    # Search entity recursively
    # Algorithm:
    # For a given entity we get recursively his parents, for each set of parents found we get recursively children (until deep 0).
    # If an entity as a set (P1,P2) as parents, we will search children if (P1,P2) set ... but not children of P1 and children of P2
    # Datas are stored in ontoClassIdLabelDeep dictionay as (classId->(label,depth))
    def __searchEntityByIdAndDeep(self, classIds: tuple, deep, ontoClassIdLabelDeep: dict, childProcessing: bool):
        deepParent = deep + 1
        deepChild = deep - 1
        for classId in classIds:
            # store entity found
            self.__addEntity(classId, ontoClassIdLabelDeep, deep)
            if not childProcessing:
                self.__searchParents(classId, deepParent, ontoClassIdLabelDeep)
            # search children until deep 0
            elif deepChild >= 0:
                self.__searchChildren((classId,), deepChild, ontoClassIdLabelDeep)
        if deepChild >= 0:
            if not childProcessing:
                self.__searchChildren(classIds, deepChild, ontoClassIdLabelDeep)

