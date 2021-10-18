
import sys
from onto_loader import OntoLoader
from onto_memory_storage import OntoMemoryStorage
from onto_finder import OntoFinder

if __name__ == '__main__':
  args = sys.argv
  ontoStorage = OntoMemoryStorage()
  loader = OntoLoader(ontoStorage)
  finder = OntoFinder(ontoStorage)
  print("Load file " + args[1])
  loader.loadFile(args[1])
  print("File loaded\n")
  ontoRelation = finder.searchEntityById("http://entity/CST/HYPOCHLOREM")
  print(ontoRelation)