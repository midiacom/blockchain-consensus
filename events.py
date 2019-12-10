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

class Event_Block_Generated(Event):
    name = "eventChangeArrived"

    def event_handler(self):
        pass


class Event_Print_Neighbors(Event):
    name = "eventShowNeighbors"

    def event_handler(self):
        pass

class Event_Generate_Block(Event):
    name = "eventGenerateBlock"

    def event_handler(self):
        pass

class Event_Send_Msg(Event):
    name = "eventSendMsg"

    def event_handler(self):
        pass
