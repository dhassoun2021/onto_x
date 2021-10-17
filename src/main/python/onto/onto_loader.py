from src.main.python.onto.onto_data import OntoData
from src.main.python.onto.onto_storage import OntoStorageInterface

#This class has responsability to read file and store data in memory structure
class OntoLoader:
    __ontoStorage:OntoStorageInterface

    def __init__(self,ontoStorage: OntoStorageInterface):
        self.ontoStorage = ontoStorage

    def __listParentsToTuple(self,parents):
        if ("|" not in parents):
            return (parents,)
        tokensParents = parents.split("|")
        return tuple(tokensParents)

    def __getOntoFromLine(self,line):
        tokens = line.split(",")
        classId = tokens[0]
        label = tokens[1]
        parents = tokens[2]
        return OntoData(classId,label,parents)

    def __storeOntoDatas(self,onto:OntoData):
        # store classId -> label
        self.ontoStorage.insertClassIdLabelOnto(onto.getClassId(), onto.getLabel())
        if (len(onto.getParents()) > 1):
            tupleParents = self.__listParentsToTuple(onto.getParents())
            # store classId->parents
            self.ontoStorage.insertClassIdParentsOnto(onto.getClassId(), tupleParents)
            # store tupe(parents)->class id of children
            self.ontoStorage.addChildToParents(tupleParents, onto.getClassId())

    def loadFile(self,name):
        f = open(name)
        i = 1
        for line in f:
            line = line.rstrip('\n')
            #ignore first line
            if i > 1:
                onto = self.__getOntoFromLine(line)
                self.__storeOntoDatas(onto)
            i = i + 1
        f.close()
