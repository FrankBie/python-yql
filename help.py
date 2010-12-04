#!/usr/bin/env python3

__all__ = [ 'yql_help' ]

import os.path

HelpPath = './help'

def yql_help(s):
    path = os.path.join(HelpPath, s)
    if os.path.exists(path):
        print(open(path).read())
        return True
    print("No help for `{}'".format(s))
    return False
