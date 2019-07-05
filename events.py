class Event:

    timestamp = None
    name = None
    params = []
    returned = None

    def __init__(self, params*):
        self.params = params
        pass

    def event_handler(self):
        pass

class EventoPrintNeighbors (Event):
    node_ID = None
    name = "eventShowNeighbors"

class GenerateBlockEvent(Event):
    node_ID = None
    name = "eventGenerateBlock"

    def __init__(self):
        pass

    @Override
    def event_handler(self):
        pass
