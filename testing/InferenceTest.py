import unittest
import sys 

sys.path.append("..")

from abm.InferenceMachine import InferenceMachine


class InferenceTest(unittest.TestCase):
    #Functional tests
    def test_add_one(self):
        inf = InferenceMachine()
        trans = inf.infere(2,3)
        self.assertEqual(trans, "add_one")

    def test_subtract_one(self):
        inf = InferenceMachine()
        trans = inf.infere(3,2)
        self.assertEqual(trans, "subtract_one")

    def test_half(self):
        inf = InferenceMachine()
        trans = inf.infere(4,2)
        self.assertEqual(trans, "half")
    
    def test_triple(self):
        inf = InferenceMachine()
        trans = inf.infere(1,3)
        self.assertEqual(trans, "triple")

    def test_detect_no_change(self):
        inf = InferenceMachine()
        trans = inf.infere(1,1)
        self.assertEqual(trans, "no_change")

    def test_detect_gap(self):
        inf = InferenceMachine()
        trans = inf.infere(5,3)
        self.assertEqual(trans, "gap_in_provenance")

if __name__ == '__main__':
    unittest.main()