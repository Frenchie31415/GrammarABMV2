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
class AdvancedL1Agent:
    def __init__(self,init_num,target):
        self.init_num = init_num
        self.target = target
    
    def start_agent(self,num_steps):
        self.app = App('AdvancedL1Agent')
        self.app.set_number(self.init_num)
        diff = abs(self.app.get_number() - self.target)
        if diff <= 10:
            self.calc_path(self.init_num,self.target)
        else:
            #Do steps in 10 step chunks + remaineder
            if self.init_num < self.target:
                sections = list(self.split(range(self.init_num,self.target),3))
            else:
                sections = list(self.split(range(self.init_num,self.target,step=-1),3))
            for x in sections:
                    self.calc_path(x[0],x[len(x)-1])

            return None
        
    def split(self,a, n):
        k, m = divmod(len(a), n)
        return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)+1] for i in range(n))
        
    def calc_path(self,start,check_point):
        pp = PossibleProvenanceMachine()
        pp.calc_graph(start,check_point)
        graph = pp.get_graph()
        paths = list(nx.all_simple_paths(graph,start,check_point))
        sorted(paths,key=len)
        dist_numerical = list(reversed(range(1,len(paths)+1))) #Creates y=-x line
        cumulative = sum(dist_numerical)
        dist = [x/cumulative for x in dist_numerical] #Creates linear dist
        choice = (np.random.choice(len(paths),1,p=dist))[0] #Selects index
        print(choice)
        path = paths[choice]

        inf = InferenceMachine()

        for i in range(0,len(path)-1):
            fr = path[i]
            to = path[i+1]
            action = inf.infere(fr,to)

            if action == "add_one":
                self.app.add_one()
            elif action == "subtract_one":
                self.app.subtract_one()
            elif action == "triple":
                self.app.triple()
            elif action == "half":
                self.app.half()




if __name__ == "__main__":
    agent = AdvancedL1Agent(101,130)
    agent.start_agent(100)