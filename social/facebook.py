import logging
from logging.handlers import SysLogHandler
from service import find_syslog, Service


class Facebook(Service):
    def __init__(self, *args, **kwargs):
        super(Facebook, self).__init__(*args, **kwargs)
        self.logger.addHandler(SysLogHandler(address=find_syslog(),
                               facility=SysLogHandler.LOG_DAEMON))
        self.logger.setLevel(logging.INFO)

    def run(self):
        self.logger.info("Started Facebook Service")
        while not self.got_sigterm():
            pass
            
