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

if __name__ == '__main__':
    unittest.main()