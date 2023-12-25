#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.realpath(__file__))
    res = os.popen("ps aux | grep run.py | grep -v grep").read()
    if not res:
        command = "nohup python3 %s/run.py &" % script_dir
        print(command)
        os.popen(command)
        print("django not running, starting...")
    else:
        print("django already running.")
