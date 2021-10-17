class OntoStorageInterface:
    def insertClassIdLabelOnto(self, classId: str, label: str):
        pass
    def insertClassIdParentsOnto(self, classId: str, parents: tuple):
        pass

    def addChildToParents(self,tupleParents:tuple, idChild:str):
        pass

    def findLabelById(self,classId:str)->str:
        pass

    def findParentsById(self,classId:str)->tuple:
        pass

    def findChildrenById(self,parents:tuple)->list:
        pass