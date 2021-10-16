ontoChildParents = dict()
ontoParentChildren = dict()
ontoClassIdLabel = dict()
ontoLabelDeep = dict()
def loadFile(name):
    f = open(name)
    i = 1
    for line in f:
        line = line.rstrip('\n')
        if i > 1:
           tokens = line.split(",")
           id = tokens[0]
           label = tokens[1]
           parents = tokens[2]
           ontoClassIdLabel[id] = label
           if (len(parents) > 1):
               listParents = parents.split("|")
               ontoChildParents[id] = listParents
               tupleParents = tuple(listParents)
               pushParentsIdChild(tupleParents,id)
        i = i+1
    f.close()

def listParentsToTuple(parents):
    if ("|" not in parents):
        return tuple(parents)
    tokensParents = parents.split("|")
    return tuple(tokensParents)

def parentsToList(parents):
    if ("|" not in parents):
        return list(parents)
    return parents.split("|")


def pushParentsIdChild(tupleParents,idChild):
    if ontoParentChildren.get(tupleParents) is None:
        ontoParentChildren[tupleParents] = []
    id:list = ontoParentChildren[tupleParents]
    id.append(idChild)

def searchEntityById(classId):
    searchEntityByIdAndDeep((classId,),0)

def searchEntityByIdAndDeep(classIds:tuple,deep):
    deepParent = deep + 1
    deepChild = deep - 1
    for classId in classIds:
        label = ontoClassIdLabel.get(classId)
        if label is not None and len(label) > 0:
            tupleLabelDeep = ontoLabelDeep.get(classId)
            if tupleLabelDeep is None:
                ontoLabelDeep[classId] = (label,deep,)
                parents = ontoChildParents[classId]
                if parents is not None and len(parents) > 0:
                    tupleParents = tuple(parents)
                    searchEntityByIdAndDeep(tupleParents,deepParent)
    if deepChild >= 0:
      children = ontoParentChildren.get(classIds)
      if children is not None and len(children) > 0:
          searchEntityByIdAndDeep(tuple(children), deepChild)

if __name__ == '__main__':
    loadFile('c:/projets/onto_x/src/resources/onto_x.csv')
    searchEntityById("http://entity/CST/CERVIX%20DIS")
    print("hello")