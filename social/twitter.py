import sys
sys.path.append("../")
import logging
import time
from logging.handlers import SysLogHandler
from service import find_syslog, Service
import models

import twitter


class Twitter(Service):
    def __init__(self, *args, **kwargs):
        super(Twitter, self).__init__(*args, **kwargs)
        self.logger.addHandler(SysLogHandler(address=find_syslog(),
                               facility=SysLogHandler.LOG_DAEMON))
        self.logger.setLevel(logging.INFO)

    def run(self):
        self.logger.info("Started Twitter Service")
        while not self.got_sigterm():
            users = models.get_all_users()
            for user in users:
                try:
                    api = twitter.Api(consumer_key='consumer_key',
                      consumer_secret='consumer_secret',
                      access_token_key=user['twitter']['token'],
                      access_token_secret=user['twitter']['secret'])
                except:
                    pass
            time.sleep(60)

