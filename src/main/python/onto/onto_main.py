import sys
from onto_loader import OntoLoader
from onto_memory_storage import OntoMemoryStorage
from onto_finder import OntoFinder

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 4:
        print("The command line should have 3 parameters")
        sys.exit(1)
    fileName = args[1]
    commandName = args[2]
    parameterQuery = args[3]
    if commandName != "searchOntoById" and commandName != "searchOntoByName":
        print("unkown commandName " + commandName)
        sys.exit(1)

    ontoStorage = OntoMemoryStorage()
    loader = OntoLoader(ontoStorage)
    finder = OntoFinder(ontoStorage)
    loader.loadFile(fileName)
    print("File loaded\n")
    if commandName == "searchOntoById":
        ontoRelation = finder.searchEntityById(parameterQuery)
        print(ontoRelation)
    elif commandName == "searchOntoByName":
        ontoRelation = finder.searchEntityByLabel(parameterQuery)
        print(ontoRelation)
