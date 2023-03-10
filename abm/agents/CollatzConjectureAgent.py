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
class CollatzConjectureAgent:
    def __init__(self,init_num):
        self.init_num = init_num
    
    def start_agent(self,num_steps):
        self.app = App('CollatzConjectureAgent')
        self.app.set_number(self.init_num)
        while(self.app.get_number() != 1):
            if self.app.get_number() % 2 == 0:
                self.app.half()
            else:
                self.app.triple()
                self.app.add_one()

if __name__ == "__main__":
    agent = CollatzConjectureAgent(101)
    agent.start_agent(100)