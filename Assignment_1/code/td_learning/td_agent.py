class TD_Agent(object):

    def __init__(self,env) -> None:
        self.env = env
        

    def make_action(self, state, test=True):

        raise NotImplementedError("Subclasses should implement this!")
    
    def train(self):

        raise NotImplementedError("Subclasses should implement this!")

 





