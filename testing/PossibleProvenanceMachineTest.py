import unittest
import networkx as nx
import sys 

sys.path.append("..")

from abm.PossibleProvenanceMachine import PossibleProvenanceMachine

class PossibleProvenanceMachineTest(unittest.TestCase):
    #Bound tests
    def test_upper_bound(self):
        pp = PossibleProvenanceMachine()
        actual_ub = pp.get_ub(2)
        exp_ub = 4
        self.assertEqual(exp_ub,actual_ub)

    def test_lower_bound_div3(self):
        pp = PossibleProvenanceMachine()
        actual_lb = pp.get_lb(3)
        exp_lb = 1
        self.assertEqual(exp_lb,actual_lb)

    def test_lower_bound_otherwise(self):
        pp = PossibleProvenanceMachine()
        actual_lb = pp.get_lb(2)
        exp_lb = 2
        self.assertEqual(exp_lb,actual_lb)

    #Depth tests
    def test_depth_smalldif(self):
        pp = PossibleProvenanceMachine()
        actual_lb = pp.get_max_depth(2,5)
        exp_lb = 9
        self.assertEqual(exp_lb,actual_lb)

    def test_depth_otherwise(self):
        pp = PossibleProvenanceMachine()
        actual_lb = pp.get_max_depth(1,12)
        exp_lb = 11
        self.assertEqual(exp_lb,actual_lb)

if __name__ == '__main__':
    unittest.main()