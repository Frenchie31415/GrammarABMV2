import random
import sys
sys.path.append('..')
from App import App

#Agent randomly adds or subtracts one (no goal number just randomly moves about)
class BeginnerAgent:
    def __init__(self,init_num):
        self.p = random.random()
        self.init_num = init_num
    
    def set_p(self,p):
        self.p = p
    
    def start_agent(self,num_steps):
        app = App('BeginnerData/BeginnerAgent')
        app.set_number(self.init_num)

        for i in range(0,num_steps):
            choice = random.random()
            if choice <= self.p:
                app.add_one()
            else:
                app.subtract_one()


if __name__ == "__main__":
    agent = BeginnerAgent(1001)
    agent.start_agent(1000)