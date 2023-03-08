import unittest
import sys 

sys.path.append("..")

from abm.App import App


class AppTest(unittest.TestCase):
    #Functional tests
    def test_setter(self):
        app = App()
        app.set_number(1)
        self.assertEqual(app.number, 1, 'Number should be one')

    def test_add_one(self):
        app = App()
        app.set_number(1)
        app.add_one()
        self.assertEqual(app.number, 2)

    def test_subtract_one(self):
        app = App()
        app.set_number(2)
        app.subtract_one()
        self.assertEqual(app.number, 1)

    def test_half(self):
        app = App()
        app.set_number(2)
        app.half()
        self.assertEqual(app.number, 1)

    def test_triple(self):
        app = App()
        app.set_number(3)
        app.triple()
        self.assertEqual(app.number, 9)       

if __name__ == '__main__':
    unittest.main()