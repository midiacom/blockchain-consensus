from Logger import LoggerAux

class Event:

    timestamp = None
    name = None
    params = []
    node_ID = None

    def __init__(self, params, logger: LoggerAux):
        """
        params[0] --> timestamp
        params[1] --> target node
        params[2:] --> event parameters
        """

        self.params = params
        self.timestamp = params[0]
        self.node = params[1]
        self.logger = logger

    def event_handler(self):
        pass


class EventRaftProposeBlock(Event):
    name = "Raft_Propose_Block"

    def event_handler(self):
        self.logger.create_log("Timestamp: {} - Event: {} - From: {}".format(self.timestamp, self.name, self.node.id))
        generated_events = self.node.callbacks["propose_block"](self.params)
        return generated_events


class EventRaftValidateBlock(Event):
    name = "Raft_Validate_Block"

    def event_handler(self):
        self.logger.create_log("Timestamp: {} - Event: {} - From: {}".format(self.timestamp, self.name, self.node.id))
        generated_events = self.node.callbacks["validate_block"](self.params)
        return generated_events


class EventRaftReceiveResponse(Event):
    name = "Raft_Receive_Response"

    def event_handler(self):
        self.logger.create_log("Timestamp: {} - Event: {} - From: {} - To: {}".format(self.timestamp, self.name, self.params[2].id, self.node.id))
        generated_events = self.node.callbacks["receive_response"](self.params)
        return generated_events
