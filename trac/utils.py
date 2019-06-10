#!/usr/bin/env python2.7
#--coding:utf-8--
"""
utils.py
"""
import time, logging, sys, os
from datetime import datetime

__author__ = "CAO Yaqiang"
__date__ = "2018-07-12"
__email__ = "caoyaqiang0410@gmail.com"


def getLogger(fn=os.getcwd() + "/" + os.path.basename(__file__) + ".log"):
    #get the current time
    date = time.strftime(' %Y-%m-%d', time.localtime(time.time()))
    #set up logging, both write log info to console and log file
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(name)-6s %(levelname)-8s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename=fn,
        filemode='a')
    logger = logging.getLogger()
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.NOTSET)
    return logger


def callSys(cmds, logger):
    """
    Call systematic commands without return.
    """
    for c in cmds:
        logger.info(c)
        try:
            os.system(c)
        except:
            logger.error(c)


def cFlush(r):
    """
    One line flush.
    """
    sys.stdout.write("\r%s" % r)
    sys.stdout.flush()


class PET(object):
    #cA is the center of left read
    __slots__ = [
        "chromA", "chromB", "startA", "startB", "endA", "endB", "strandA",
        "strandB", "cA", "cB", "distance", "cis"
    ]

    def __init__(self, d):
        """
        d is line = line.split( "\n" )[ 0 ].split( "\t" ) from BEDPE file 
        """
        self.chromA = d[0]
        self.startA = int(d[1])
        self.endA = int(d[2])
        self.strandA = d[8]
        self.chromB = d[3]
        self.startB = int(d[4])
        self.endB = int(d[5])
        self.strandB = d[9]
        self.cis = False
        if self.chromA == self.chromB:
            self.cis = True
            self.cA = (self.startA + self.endA) / 2
            self.cB = (self.startB + self.endB) / 2
            self.distance = abs(self.cB - self.cA)