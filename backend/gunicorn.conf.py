import sys
import os
import logging
import logging.handlers
from logging.handlers import WatchedFileHandler
import multiprocessing

BASE_DIR = '/home/ubuntu/project/SOF106-Project/backend'
sys.path.append(BASE_DIR)

LOG_DIR = os.path.join(BASE_DIR, 'log')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

bind = "0.0.0.0:8000"

daemon = True

# the number of connections can be handled
backlog = 512

timeout = 30

debug = False

# gunicorn working dir
chdir = BASE_DIR

# defalut to sync, other: eventlet, gevent, or tornado, gthread, gaiohttpjkkk
worker_class = 'sync'

workers = multiprocessing.cpu_count()
# threads under each worker
threads = multiprocessing.cpu_count() * 2

# debug、info、warning、error、critical
loglevel = 'info'

# log format
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'
'''
h          remote address
l          '-'
u          currently '-', may be user name in future releases
t          date of the request
r          status line (e.g. ``GET / HTTP/1.1``)
s          status
b          response length or '-'
f          referer
a          user agent
T          request time in seconds
D          request time in microseconds
L          request time in decimal seconds
p          process ID
'''

accesslog = os.path.join(LOG_DIR, 'gunicorn_access.log')
errorlog = os.path.join(LOG_DIR, 'gunicorn_error.log')
# pid
pidfile = os.path.join(LOG_DIR, 'gunicorn_error.pid')

# std out
accesslog = "-"
errorlog = "-"

# process name
proc_name = 'hippiezhou_fun.pid'
