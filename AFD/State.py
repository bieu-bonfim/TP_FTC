class State:
    def __init__(self, number, transitions):
        self.number = number
        self.transitions = transitions

    def get_next(self, read):
        return self.transitions[read]
