# coding=utf-8

import sys
import logging
import matplotlib.pyplot

logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format='[%(asctime)s] [%(filename)s:%(lineno)d] [%(levelname)s] %(message)s',)
logger = logging.getLogger()

logging.getLogger('matplotlib').setLevel(logging.WARNING)
logging.getLogger("PIL").setLevel(logging.WARNING)
logging.getLogger("fontTools").setLevel(logging.WARNING)
