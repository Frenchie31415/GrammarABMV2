import random
import sys
import numpy as np
sys.path.append('..')
from App import App

#Agent randomly adds or subtracts one (no goal number just randomly moves about)
class IntermediateL1Agent:
    def __init__(self,init_num,target):
        if init_num < target:
            dist = [0.27,0.23,0.27,0.23]
        else:
            dist = [0.23,0.27,0.23,0.27]
        cumulative = sum(dist)
        self.add_one = dist[0] / cumulative
        self.subtract_one = dist[1] / cumulative
        self.triple = dist[2] / cumulative
        self.half = dist[3] / cumulative
        self.init_num = init_num
        self.dist = [self.add_one,self.subtract_one,self.triple,self.half]
    
    def set_dist(self,dist):
        self.dist = dist
        cumulative = sum(dist)
        self.add_one = dist[0] / cumulative
        self.subtract_one = dist[1] / cumulative
        self.triple = dist[2] / cumulative
        self.half = dist[3] / cumulative
    
    def start_agent(self,num_steps):
        app = App('IntermediateL1Agent')
        app.set_number(101)

        #Find way to select option with random distribution
        for i in range(0,num_steps):
            self.perform_action(app)

    def perform_action(self,app):
        choice = np.random.choice(4,1,p=self.dist)
        if choice == 0:
            app.add_one()
        elif choice == 1:
            app.subtract_one()
        elif choice == 2:
            app.triple()
        else:
            if app.get_number() % 2 == 0:
                app.half()
            else:
                self.perform_action(app)

if __name__ == "__main__":
    agent = IntermediateL1Agent(101,500)
    agent.start_agent(100)