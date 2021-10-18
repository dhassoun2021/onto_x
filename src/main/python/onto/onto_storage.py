#Expose method to store data from onto
class OntoStorageInterface:

    #store association classId and label
    def insertClassIdLabelOnto(self, classId: str, label: str):
        pass

    # store association label and classId
    def insertLabelClassIdOnto(self, classId: str, label: str):
        pass

     #store association classId and parents
    def insertClassIdParentsOnto(self, classId: str, parents: tuple):
        pass

    #Associate child to parents
    def addChildToParents(self,tupleParents:tuple, idChild:str):
        pass

    #Find label from classId
    def findLabelById(self,classId:str)->str:
        pass

    # Find classId from label
    def findClassIdByLabel(self, label: str) -> str:
        pass

    #Find parents from classId
    def findParentsById(self,classId:str)->tuple:
        pass

    #Find children from parents
    def findChildren(self,parents:tuple)->list:
        pass