import unittest
import sys
sys.path.append('../../../main/python/onto')
from src.main.python.onto.onto_loader import OntoLoader
from src.main.python.onto.onto_memory_storage import OntoMemoryStorage
from src.main.python.onto.onto_finder import OntoFinder


class OntoTest(unittest.TestCase):
    __ontoStorage = OntoMemoryStorage()

    def setUp(self):
        loader = OntoLoader(self.__ontoStorage)
        loader.loadFile("../../resources/onto_test.csv")


    def tearDown(self):
        pass

    def test_findHypochloremByIdShouldSuccess(self):
        finder = OntoFinder(self.__ontoStorage)
        ontoLabelDeep = finder.searchEntityById("http://entity/CST/HYPOCHLOREM")
        self.assertIsNotNone(ontoLabelDeep)
        self.assertEqual(len(ontoLabelDeep),4)
        self.assertEqual(ontoLabelDeep.get(("http://entity/CST/HYPOCHLOREM","HYPOCHLOREMIA")),0)
        self.assertEqual(ontoLabelDeep.get(("http://entity/CST/METGEN","METGEN")), 1)
        self.assertEqual(ontoLabelDeep.get(("http://entity/CST/MAN/ION/CL","CL")), 1)
        self.assertEqual(ontoLabelDeep.get(("http://entity/CST/MET","MET")), 0)

    def test_findHypochloremByIdWithEmptyIdShouldReturnEmptyResult(self):
        finder = OntoFinder(self.__ontoStorage)
        ontoLabelDeep = finder.searchEntityById("id")
        self.assertIsNotNone(ontoLabelDeep)
        self.assertIsNotNone(ontoLabelDeep)
        self.assertEqual(dict(), ontoLabelDeep)

    def test_findHypochloremByNameShouldSuccess(self):
        finder = OntoFinder(self.__ontoStorage)
        ontoLabelDeep = finder.searchEntityByLabel("HYPOCHLOREMIA")
        self.assertIsNotNone(ontoLabelDeep)
        self.assertEqual(4, len(ontoLabelDeep))
        self.assertEqual(ontoLabelDeep.get(("http://entity/CST/HYPOCHLOREM", "HYPOCHLOREMIA")), 0)
        self.assertEqual(ontoLabelDeep.get(("http://entity/CST/METGEN", "METGEN")), 1)
        self.assertEqual(ontoLabelDeep.get(("http://entity/CST/MAN/ION/CL", "CL")), 1)
        self.assertEqual(ontoLabelDeep.get(("http://entity/CST/MET", "MET")), 0)

    def test_findHypochloremByNameWithLowerCaseShouldSuccess(self):
        finder = OntoFinder(self.__ontoStorage)
        ontoLabelDeep = finder.searchEntityByLabel("hypochloremia")
        self.assertIsNotNone(ontoLabelDeep)
        self.assertEqual(4, len(ontoLabelDeep))
        self.assertEqual(ontoLabelDeep.get(("http://entity/CST/HYPOCHLOREM", "HYPOCHLOREMIA")), 0)
        self.assertEqual(ontoLabelDeep.get(("http://entity/CST/METGEN", "METGEN")), 1)
        self.assertEqual(ontoLabelDeep.get(("http://entity/CST/MAN/ION/CL", "CL")), 1)
        self.assertEqual(ontoLabelDeep.get(("http://entity/CST/MET", "MET")), 0)

    def test_findHypochloremByNameNotFoundShouldReturnEmptyResult(self):
        finder = OntoFinder(self.__ontoStorage)
        ontoLabelDeep = finder.searchEntityByLabel("hyp")
        self.assertIsNotNone(ontoLabelDeep)
        self.assertEqual(dict(), ontoLabelDeep)

   # def test_All(self):
    #    storage = OntoMemoryStorage()
     #   loader = OntoLoader(storage)
      #  loader.loadFile("C:/projets/onto_x/src/main/resources/onto_x.csv")
       # finder = OntoFinder(storage)
        #result = finder.searchEntityById("http://entity/CST/CERVIX%20DIS")
        #print(len(result.keys()))

if __name__ == '__main__':
    unittest.main()