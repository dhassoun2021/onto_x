import sys
from onto_loader import OntoLoader
from onto_memory_storage import OntoMemoryStorage
from onto_finder import OntoFinder

# Entry point to use application
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
    loader.load_file(fileName)
    print("File " + fileName + " loaded\n")
    if commandName == "searchOntoById":
        ontoRelation = finder.search_entity_by_id(parameterQuery)
        print(ontoRelation)
    elif commandName == "searchOntoByName":
        ontoRelation = finder.search_entity_by_label(parameterQuery)
        print(ontoRelation)
