import unittest
import sys 

sys.path.append("..")

from abm.InferenceMachine import InferenceMachine


import unittest
import sys 

sys.path.append("..")

import abm.Evaluators as eval

class EvaluationTest(unittest.TestCase):
    #Functional tests
    def test_node_accuracy_100(self):
        input_expected = [1,2,3,4]
        input_actual = [1,2,3,4]
        self.assertEqual(eval.node_accuracy(input_actual,input_expected), 100.0)

    def test_node_accuracy_50(self):
        input_expected = [1,2,3,4]
        input_actual = [1,2,8,9]
        self.assertEqual(eval.node_accuracy(input_actual,input_expected), 50.0)

    def test_node_accuracy_0(self):
        input_expected = [1,2,3,4]
        input_actual = [6,7,8,9]
        self.assertEqual(eval.node_accuracy(input_actual,input_expected), 0.0)

    def test_node_accuracy_75(self):
        input_expected = [1,2,3,6,4]
        input_actual = [1,2,5,4]
        self.assertEqual(eval.node_accuracy(input_actual,input_expected), 60.0)

if __name__ == '__main__':
    unittest.main()