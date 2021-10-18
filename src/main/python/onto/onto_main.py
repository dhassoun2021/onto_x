
import sys
from onto_loader import OntoLoader
from onto_memory_storage import OntoMemoryStorage
from onto_finder import OntoFinder

if __name__ == '__main__':
  args = sys.argv
  fileName = args[1]
  commandName = args[2]
  parameterQuery = args[3]
  ontoStorage = OntoMemoryStorage()
  loader = OntoLoader(ontoStorage)
  finder = OntoFinder(ontoStorage)
  loader.loadFile(fileName)
  print("File loaded\n")
  ontoRelation = finder.searchEntityById(parameterQuery)
  print(ontoRelation)