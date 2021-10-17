ontoChildParents = dict()
ontoParentChildren = dict()
ontoClassIdLabel = dict()

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
    ontoClassIdLabelDeep = dict()
    searchEntityByIdAndDeep((classId,),0,ontoClassIdLabelDeep)
    ontoLabelDeep = ontoIdClassLabelDeepToOntoLabelDeep(ontoClassIdLabelDeep)
    return ontoLabelDeep

def ontoIdClassLabelDeepToOntoLabelDeep(ontoClassIdLabelDeep:dict):
    ontoLabelDeep = dict()
    values = ontoClassIdLabelDeep.values()
    for value in values:
        label = value[0]
        deep = value[1]
        ontoLabelDeep[label] = deep
    return ontoLabelDeep

def isOntoProcessed (classId,ontoClassIdLabelDeep):
    return ontoClassIdLabelDeep.get(classId) is None

def searchEntityByIdAndDeep(classIds:tuple,deep,ontoClassIdLabelDeep):
    deepParent = deep + 1
    deepChild = deep - 1
    for classId in classIds:
        label = ontoClassIdLabel.get(classId)
        if label is not None and len(label) > 0:
            if isOntoProcessed(classId,ontoClassIdLabelDeep):
                ontoClassIdLabelDeep[classId] = (label,deep,)
                parents = ontoChildParents.get(classId)
                if parents is not None and len(parents) > 0:
                    tupleParents = tuple(parents)
                    searchEntityByIdAndDeep(tupleParents,deepParent,ontoClassIdLabelDeep)
    if deepChild >= 0:
      children = ontoParentChildren.get(classIds)
      if children is not None and len(children) > 0:
          searchEntityByIdAndDeep(tuple(children), deepChild,ontoClassIdLabelDeep)

if __name__ == '__main__':
    loadFile('c:/projets/onto_x/src/main/resources/onto_test.csv')
    ontoClassIdLabelDeep = searchEntityById("http://entity/CST/HYPOCHLOREM")
    print(ontoClassIdLabelDeep)