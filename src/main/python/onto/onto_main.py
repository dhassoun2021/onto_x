from src.main.python.onto.onto_loader import OntoLoader
from src.main.python.onto.onto_finder import OntoFinder
from src.main.python.onto.onto_memory_storage import OntoMemoryStorage
import sys
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