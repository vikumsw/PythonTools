# !/usr/bin/python

import os, sys

cmd = r'git tag -a "tagcheck1" -m "test"'

def exec_command(cmd):
    print(os.popen(cmd,'r'))


#exec_command(r'git checkout master')
exec_command(r'git pull')