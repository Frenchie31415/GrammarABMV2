import random

class StocasticModel:
    def __init__(self,language,history):
        self.language = language
        self.history = history

    def predict_prov_path(self,trans_paths):
        path_index = random.randint(0,len(trans_paths)-1)
        return trans_paths[path_index]
