import random
import sys
import numpy as np
sys.path.append('..')
from App import App

#Agent randomly adds or subtracts one (no goal number just randomly moves about)
class IntermediateL4Agent:
    def __init__(self,init_num,target):
        self.target = target

        if init_num < target:
            dist = [0.4,0.1,0.4,0.1]
        else:
            dist = [0.1,0.4,0.1,0.4]

        cumulative = sum(dist)
        self.add_one = dist[0] / cumulative
        self.subtract_one = dist[1] / cumulative
        self.triple = dist[2] / cumulative
        self.half = dist[3] / cumulative
        self.init_num = init_num

    def check_direction(self,app):
        current_num = app.get_number()
        if current_num < self.target:
            self.dist = [0.4,0.1,0.4,0.1]
        else:
            self.dist = [0.1,0.4,0.1,0.4]
    
    def set_dist(self,dist):
        self.dist = dist
        cumulative = sum(dist)
        self.add_one = dist[0] / cumulative
        self.subtract_one = dist[1] / cumulative
        self.triple = dist[2] / cumulative
        self.half = dist[3] / cumulative
    
    def start_agent(self,num_steps):
        app = App('IntermediateL4Agent')
        app.set_number(101)

        #Find way to select option with random distribution
        for i in range(0,num_steps):
            if i % 3 == 0:
                self.check_direction(app)

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
    agent = IntermediateL4Agent(101)
    agent.start_agent(100)