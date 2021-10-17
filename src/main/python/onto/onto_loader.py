from src.main.python.onto.onto_storage import OntoStorageInterface


class OntoLoader:
    ontoStorage:OntoStorageInterface

    def __init__(self,ontoStorage: OntoStorageInterface):
        self.ontoStorage = ontoStorage

    def listParentsToTuple(self,parents):
        if ("|" not in parents):
            return (parents,)
        tokensParents = parents.split("|")
        return tuple(tokensParents)



    def loadFile(self,name):
        f = open(name)
        i = 1
        for line in f:
            line = line.rstrip('\n')
            #ignore first line
            if i > 1:
                tokens = line.split(",")
                id = tokens[0]
                label = tokens[1]
                parents = tokens[2]
                self.ontoStorage.insertClassIdLabelOnto(id,label)
                if (len(parents) > 1):
                    tupleParents = self.listParentsToTuple(parents)
                    self.ontoStorage.insertClassIdParentsOnto(id,tupleParents)
                    self.ontoStorage.addChildToParents(tupleParents, id)
            i = i + 1
        f.close()
