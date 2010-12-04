#!/usr/bin/env python3

import os

__all__ = [ 'Pager' ]

class Pager(object):
    def __init__(_):
        _.p = os.popen('more', 'w')

    def write(_, data):
        return _.p.write(data)

    def close(_):
        _.p.close()
