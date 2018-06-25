from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('SalusMind',
             broker = 'redis://',
             backend = 'redis://',
             include = ['SalusMind.tasks'])

if __name__ == '__main__':
    app.start()
