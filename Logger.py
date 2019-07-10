import logging

class Logger_Aux:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # create a file handler
        handler = logging.FileHandler('logguizinho.log')
        handler.setLevel(logging.INFO)

        # create a logging format
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)

        # add the handlers to the logger
        self.logger.addHandler(handler)


    def create_log(self, event):
        self.logger.info("ID: {} - Timestamp: {} - Event: {}".format(event.node_ID, event.timestamp, type(event).__name__))

Logger = Logger_Aux()
