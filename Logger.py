import logging
from raft_events import *

class LoggerAux:

    def __init__(self, file_name):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)


        # create a file handler
        handler = logging.FileHandler(file_name, 'w')
        handler.setLevel(logging.INFO)

        # create a logging format
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)

        # add the handlers to the logger
        self.logger.addHandler(handler)

    def create_log(self, msg: str):
        self.logger.info(msg)
        #self.logger.info("Timestamp: {} - Event: {} - Node: {} ".format(event.timestamp, event.name, event.node.id))

