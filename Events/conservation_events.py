from Events import Event


class EventBlockGenerated(Event):
    name = "eventChangeArrived"

    def event_handler(self):
        pass


class EventPrintNeighbors(Event):
    name = "eventShowNeighbors"

    def event_handler(self):
        pass


class EventGenerateBlock(Event):
    name = "eventGenerateBlock"

    def event_handler(self):
        pass

class EventSendMsg(Event):
    name = "eventSendMsg"

    def event_handler(self):
        pass
