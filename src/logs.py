import os
from time import strftime, gmtime 
import logging

def config_logging():
    if not os.path.exists('logs'):
        os.makedirs('logs')

    logging.basicConfig(
        filename=f"logs/{strftime('%Y-%m-%d--%H-%M-%S', gmtime())}.log", 
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s: %(message)s'
        )
