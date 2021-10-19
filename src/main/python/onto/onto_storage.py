#Expose method to store entity data
class OntoStorageInterface:

    #store association classId and label
    def insertClassIdLabelOnto(self, class_id: str, label: str):
        pass

    # store association label and classId
    def insertLabelClassIdOnto(self, class_id: str, label: str):
        pass

     # store association classId and parents
    def insertClassIdParentsOnto(self, class_id: str, parents: tuple):
        pass

    # Associate child to parents
    def addChildToParents(self, tuple_parents:tuple, id_child: str):
        pass

    # Find label from classId
    def findLabelById(self,class_id: str) -> str:
        pass

    # Find classId from label
    def findClassIdByLabel(self, label: str) -> str:
        pass

    # Find parents from classId
    def findParentsById(self, class_id: str) -> tuple:
        pass

    # Find children from parents
    def findChildren(self, parents: tuple) -> list:
        pass