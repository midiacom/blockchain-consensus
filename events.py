class Event:

    timestamp = None
    name = None
    params = []
    returned = None
    node_ID = None

    def __init__(self, params):
        self.params = params
        self.timestamp = params[0]
        self.node_ID = params[1]

        pass

    def event_handler(self):
        pass

class EventBlockGenerated(Event):
    name = "eventChangeArrived"

    def event_handler(self):
        pass
    
class EventoPrintNeighbors (Event):
    name = "eventShowNeighbors"

    def event_handler(self):
        pass

class GenerateBlockEvent(Event):
    name = "eventGenerateBlock"

    def event_handler(self):
        pass
