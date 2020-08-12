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

    def __lt__(self, other):
        return 1

    def event_handler(self):
        pass
