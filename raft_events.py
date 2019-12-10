

class Event:

    timestamp = None
    name = None
    params = []
    node_ID = None

    def __init__(self, params):
        """
        params[0] --> timestamp
        params[1] --> target node
        params[2:] --> event parameters
        """

        self.params = params
        self.timestamp = params[0]
        self.node = params[1]

    def event_handler(self):
        pass


class EventRaftProposeBlock(Event):
    name = "Raft_Propose_Block"

    def event_handler(self):
        generated_events = self.node.callbacks["propose_block"](self.params)
        return generated_events


class EventRaftValidateBlock(Event):
    name = "Raft_Validate_Block"

    def event_handler(self):
        generated_events = self.node.callbacks["validate_block"](self.params)
        return generated_events


class EventRaftReceiveResponse(Event):
    name = "Raft_Receive_Response"

    def event_handler(self):
        generated_events = self.node.callbacks["receive_response"](self.params)
        return generated_events
