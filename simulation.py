import heapq


class Simulation:

    event_flow = []

    def __init__(self, simulation_steps, nodes, event_flow):

        self.simulation_steps = simulation_steps
        self.nodes = nodes
        for event in event_flow:
            heapq.heappush(self.event_flow, (event.timestamp, event))

    def run(self):

        while self.event_flow:
            current_event = heapq.heappop(self.event_flow)
            if current_event[0] < self.simulation_steps:
                returned_events = current_event[1].event_handler()
                if returned_events:
                    for e in returned_events:
                        heapq.heappush(self.event_flow, (e.timestamp, e))
            else:
                break
