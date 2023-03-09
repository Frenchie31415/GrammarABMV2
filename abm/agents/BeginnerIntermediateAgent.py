import random
import sys
import numpy as np
sys.path.append('..')
from App import App

#Agent randomly adds or subtracts one (no goal number just randomly moves about)
class BeginnerIntermediateAgent:
    def __init__(self,init_num):
        dist = [random.random(),random.random(),random.random(),random.random()]
        cumulative = sum(dist)
        self.add_one = dist[0] / cumulative
        self.subtract_one = dist[1] / cumulative
        self.triple = dist[2] / cumulative
        self.half = dist[3] / cumulative
        self.init_num = init_num
    
    def set_dist(self,dist):
        self.dist = dist
        cumulative = sum(dist)
        self.add_one = dist[0] / cumulative
        self.subtract_one = dist[1] / cumulative
        self.triple = dist[2] / cumulative
        self.half = dist[3] / cumulative
    
    def start_agent(self,num_steps):
        app = App('BeginnerIntermediateAgent')
        app.set_number(101)

        #Find way to select option with random distribution
        for i in range(0,num_steps):
            choice = np.random.choice(4,1,p=self.dist)
            if choice == 0:
                app.add_one()
            elif choice == 1:
                app.subtract_one()
            elif choice == 2:
                app.triple()
            else:
                app.half()


if __name__ == "__main__":
    agent = BeginnerIntermediateAgent(101)
    agent.start_agent(100)