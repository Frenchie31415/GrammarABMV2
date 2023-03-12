import logging
from InferenceMachine import InferenceMachine
import itertools

class Simulator:
    def __init__(self,file_name):
        self.file_name = file_name

    def init_data(self):
        inf = InferenceMachine()
        inf.set_log_path(self.file_name)
        inf.parse_log()
        self.states = inf.historical_states()
        self.transf = inf.historical_transitions()
        self.state_instances = []
        self.transf_instances = []
        self.create_instances(self.states.copy(),self.transf.copy())
        #Create splits of data
        self.state_splits = []
        self.tranf_splits = []
        self.test_split = 0
        
        #I feel like this is a poor ds
        self.train_transf = []
        self.train_states = []
        self.test_transf = []
        self.test_states = []

    #Parse COPY of states and transf as argument to retain data in class
    def create_instances(self,states,transf):
        if len(states) <= 10:
            return None
        self.state_instances.append(states[0:10])
        self.transf_instances.append(transf[0:8])
        self.create_instances(states[9:],transf[8:]) #Recursive call

    #Rotates testing fold for cross validation
    def next_fold(self):
        splits = self.splits.copy()
        #Needs to be mod
        self.test_split = self.test_split + 1
        
        self.test = splits[self.test_split % 5]
        del splits[(self.test_split % 5)]
        self.train = list(itertools.chain.from_iterable(splits))
    
    


    
if __name__ == "__main__":
    a = [1,2,3,4,5,6,7,8,9,10]
    print(a[9:])
    #sim = Simulator("agents/BeginnerData/BeginnerAgent")