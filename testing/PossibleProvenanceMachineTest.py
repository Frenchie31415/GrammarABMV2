import unittest
import networkx as nx
import sys 

from abm.PossibleProvenanceMachine import PossibleProvenanceMachine

class PossibleProvenanceMachineTest(unittest.TestCase):
    #Functional tests
    def test_one_to_two(self):
        pp = PossibleProvenanceMachine()
        exp_graph = nx.read_adjlist("testing_graphs/1to2.adj")  
        pp.calc_graph(1,2) 
        actual_graph = pp.get_graph()
        self.assertEqual(exp_graph, actual_graph)

    def test_two_to_one(self):
        pp = PossibleProvenanceMachine()
        exp_graph = nx.read_adjlist("testing_graphs/2to1.adj")
        pp.calc_graph(2,1)    
        actual_graph = pp.get_graph()
        self.assertEqual(exp_graph, actual_graph)

    def test_four_to_one(self):
        pp = PossibleProvenanceMachine()
        exp_graph = nx.read_adjlist("testing_graphs/4to1.adj")
        pp.calc_graph(4,1)   
        actual_graph = pp.get_graph()
        self.assertEqual(exp_graph, actual_graph)
    
    def test_three_to_two(self):
        pp = PossibleProvenanceMachine()
        exp_graph = nx.read_adjlist("testing_graphs/3to2.adj")   
        pp.calc_graph(3,1)   
        actual_graph = pp.get_graph()
        self.assertEqual(exp_graph, actual_graph)

    #Bound tests
    def test_upper_bound(self):
        pp = PossibleProvenanceMachine()
        exp_ub = pp.get_ub(2)
        actual_ub = 4
        self.assertEqual(exp_ub,actual_ub)

    def test_lower_bound_div3(self):
        pp = PossibleProvenanceMachine()
        exp_lb = pp.get_lb(3)
        actual_lb = 1
        self.assertEqual(exp_lb,actual_lb)

    def test_lower_bound_otherwise(self):
        pp = PossibleProvenanceMachine()
        exp_lb = pp.get_lb(2)
        actual_lb = 2
        self.assertEqual(exp_lb,actual_lb)

    #Depth tests
    def test_depth_smalldif(self):
        pp = PossibleProvenanceMachine()
        exp_lb = pp.get_depth(2,5)
        actual_lb = 9
        self.assertEqual(exp_lb,actual_lb)

    def test_depth_otherwise(self):
        pp = PossibleProvenanceMachine()
        exp_lb = pp.get_depth(1,12)
        actual_lb = 11
        self.assertEqual(exp_lb,actual_lb)

if __name__ == '__main__':
    unittest.main()