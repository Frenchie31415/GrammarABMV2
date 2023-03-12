from InferenceMachine import InferenceMachine
import pandas as pd

class Simulator:
    def __init__(self,file_name):
        self.file_name = file_name
        self.init_data()

    def init_data(self):
        inf = InferenceMachine()
        inf.set_log_path(self.file_name)
        inf.parse_log()
        self.states = inf.historical_states
        self.transf = inf.historical_transitions
        self.state_instances = []
        self.transf_instances = []
        self.start_states = []
        self.final_states = []
        self.create_instances(self.states.copy(),self.transf.copy())
        #FROM THIS POINT ONWARDS, only reference the dataframe when modelling
        self.df = pd.DataFrame({'transformations': self.transf_instances,
                           'start_states': self.start_states,
                           'final_states': self.final_states,
                          'states': self.state_instances})

    #Parse COPY of states and transf as argument to retain data in class
    def create_instances(self,states,transf):
        if len(states) <= 10:
            return None
        self.state_instances.append(states[0:10])
        self.start_states.append(states[0])
        self.final_states.append(states[9])
        self.transf_instances.append(transf[0:8])
        self.create_instances(states[9:],transf[8:]) #Recursive call
    
    
    
if __name__ == "__main__":
    sim = Simulator("agents/BeginnerData/BeginnerAgent.log")