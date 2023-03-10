import random
import sys
import numpy as np
from scipy.stats import skewnorm
import networkx as nx
sys.path.append('..')
from App import App
from PossibleProvenanceMachine import PossibleProvenanceMachine
from InferenceMachine import InferenceMachine


#Agent randomly adds or subtracts one (no goal number just randomly moves about)
class CCStocasticAgent:
    def __init__(self,init_num):
        self.init_num = init_num
    
    def start_agent(self,num_steps):
        self.app = App('CCStocasticAgent')
        self.app.set_number(self.init_num)
        using_collatz = True
        cur_steps = 1
        while(self.app.get_number() != 1 and num_steps != cur_steps):
            rnd_num = random.random()
            if rnd_num < 0.15 and using_collatz == True:
                using_collatz = not(using_collatz)
            
            if using_collatz == True:
                self.cc_action()
                cur_steps = cur_steps + 1
            else:
                self.rnd_action()
                cur_steps = cur_steps + 1
            
    def cc_action(self):
        if self.app.get_number() % 2 == 0:
            self.app.half()
        else:
            self.app.triple()
            self.app.add_one()

    def rnd_action(self):
        rnd_num = random.randint(1,2)
        if rnd_num == 1:
            self.app.add_one()
        elif rnd_num == 2:
            self.app.subtract_one()



if __name__ == "__main__":
    agent = CCStocasticAgent(101)
    agent.start_agent(100)