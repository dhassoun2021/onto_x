from src.main.python.onto.onto_loader import OntoLoader
from src.main.python.onto.onto_finder import OntoFinder
from src.main.python.onto.onto_memory_storage import OntoMemoryStorage
if __name__ == '__main__':
  ontoStorage = OntoMemoryStorage()
  loader = OntoLoader(ontoStorage)
  finder = OntoFinder(ontoStorage)
  loader.loadFile('c:/projets/onto_x/src/main/resources/onto_x.csv')
  ontoRelation = finder.searchEntityById("http://entity/CST/SKIN/SBGL")
  print(ontoRelation)