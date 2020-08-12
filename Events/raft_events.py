from Events import Event


class EventRaftProposeBlock(Event):
    '''
    params[0] --> timestamp
    params[1] --> target node
    '''

    name = "Raft_Propose_Block"

    def event_handler(self):
        generated_events = self.node.callbacks["propose_block"](self.params)
        return generated_events


class EventRaftValidateBlock(Event):
    '''
        params[0] --> timestamp
        params[1] --> target node
        params[2] --> block
        params[3] --> proposer
    '''

    name = "Raft_Validate_Block"

    def event_handler(self):
        generated_events = self.node.callbacks["validate_block"](self.params)
        return generated_events


class EventRaftReceiveResponse(Event):
    '''
        params[0] --> timestamp
        params[1] --> target node
        params[2] -->proposer
        params[3] --> response
        params[4] --> block
    '''

    name = "Raft_Receive_Response"

    def event_handler(self):
        generated_events = self.node.callbacks["receive_response"](self.params)
        return generated_events


class EventRaftAppendBlock(Event):
    '''
        params[0] --> timestamp
        params[1] --> target node
        params[2] --> block
    '''

    name = "Raft_Append_Block"

    def event_handler(self):
        generated_events = self.node.callbacks["append_block"](self.params)
        return  generated_events
