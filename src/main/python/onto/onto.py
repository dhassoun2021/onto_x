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

if __name__ == '__main__':
    loadFile('c:/projets/onto_x/src/resources/onto_x.csv')