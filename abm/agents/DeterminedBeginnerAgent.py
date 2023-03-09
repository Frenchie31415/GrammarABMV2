import random
import sys
sys.path.append('..')
from App import App

#Agent uses plus one or minus one to move towards target
class DeterminedBeginnerAgent:
    def __init__(self,init_num,target_num):
        self.init_num = init_num
        self.target_num = target_num
    
    def start_agent(self,num_steps):
        app = App('DeterminedBeginnerAgent')
        app.set_number(101)

        for i in range(0,num_steps):
            if self.init_num < self.target_num:
                app.add_one()
            elif self.init_num > self.target_num:
                app.subtract_one()
            else:
                break
            

if __name__ == "__main__":
    agent = DeterminedBeginnerAgent(101)
    agent.start_agent(100)