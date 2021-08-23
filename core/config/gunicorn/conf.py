import multiprocessing

name = 'mapa_microbiano'
loglevel = 'info'
errorlog = '-'
accesslog = '-'
workers = multiprocessing.cpu_count() * 2 + 1