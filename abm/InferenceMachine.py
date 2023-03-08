import re

class InferenceMachine:
    def __init__(self):
        self.historical_states = []
        self.historical_transitions = []
        self.log_path = None

    def set_log_path(self,path):
        self.log_path = path

    def parse_log(self):
        with open(self.log_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                data = line.split(":")[2].strip()
                state = int(re.search(r'-?\d+', data).group())
                self.historical_states.append(state)
        
        for i in range(0,len(self.historical_states)-1):
            fr = self.historical_states[i]
            to = self.historical_states[i+1]
            trans = self.infere(fr,to)
            self.historical_transitions.append(trans)

    def infere(self,fr,to):
        if fr == to:
            return "no_change"
        elif fr + 1 == to:
            return "add_one"
        elif fr - 1 == to:
            return "subtract_one"
        elif fr / 2 == to:
            return "half"
        elif fr * 3 == to:
            return "triple"
        else:
            return "gap_in_provenance"
        
if __name__ == "__main__":
    inf = InferenceMachine()
    inf.set_log_path("AppLog.log")
    inf.parse_log()