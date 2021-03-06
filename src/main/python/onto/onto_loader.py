from onto_data import EntityData
from onto_storage import OntoStorageInterface


# This class has responsability to read file and store data in memory structure



class OntoLoader:
    PARENT_LIST_SEPARATOR = "|"
    LINE_SEPARATOR = ","
    __ontoStorage: OntoStorageInterface

    def __init__(self,ontoStorage: OntoStorageInterface):
        self.ontoStorage = ontoStorage

    # Load csv file of path name, and store data
    def load_file(self, name):
        f = open(name)
        i = 1
        for line in f:
            # ignore first line
            if i > 1:
                entity = self.__get_entity_from_line(line)
                self.__store_entity_datas(entity)
            i = i + 1
        f.close()

    # convert liste parents to tuple of parents
    def __listParentsToTuple(self,parents):
        if self.PARENT_LIST_SEPARATOR not in parents:
            if (parents is None or len(parents) == 0):
                return ()
            return (parents,)
        tokensParents = parents.split(self.PARENT_LIST_SEPARATOR)
        return tuple(tokensParents)

    # Build entity data from line
    def __get_entity_from_line(self, line):
        line = line.rstrip('\n')
        tokens = line.split(self.LINE_SEPARATOR)
        classId = tokens[0]
        label = tokens[1]
        parents = tokens[2]
        tupleParents = self.__listParentsToTuple(parents)
        return EntityData(classId, label, tupleParents)

    # Store datas
    def __store_entity_datas(self, onto: EntityData):
        # store classId -> label
        self.ontoStorage.insertClassIdLabelOnto(onto.getClassId(), onto.getLabel())
        self.ontoStorage.insertLabelClassIdOnto(onto.getClassId(), onto.getLabel().upper())
        if len(onto.getParents()) > 0:
            # store classId->parents
            self.ontoStorage.insertClassIdParentsOnto(onto.getClassId(), onto.getParents())
            # store tupe(parents)->class id of children
            self.ontoStorage.addChildToParents(onto.getParents(), onto.getClassId())
