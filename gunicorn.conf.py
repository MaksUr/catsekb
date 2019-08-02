import multiprocessing

bind = '0.0.0.0:80'
workers = multiprocessing.cpu_count()
errorlog = '/var/log/gunicorn/error.log'
accesslog = '/var/log/gunicorn/access.log'
loglevel = 'info'
proc_name = 'catsekb.ru'
pidfile = './gunicorn.pid'
uid = 'www-data'
gid = 'www-data'
reload = True
