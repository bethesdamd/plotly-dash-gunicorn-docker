pidfile = 'graph.pid'
# worker_tmp_dir = ''
worker_class = 'gthread'
workers = 2
worker_connections = 1000
timeout = 30
keepalive = 2
threads = 4
proc_name = 'graph'
bind = '0.0.0.0:8080'
backlog = 2048
accesslog = '-'
errorlog = '-'
user = 'david'

