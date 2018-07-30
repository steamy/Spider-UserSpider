#!/usr/bin/python3 
# -*- coding: utf-8 -*-
# Filename:  clean_log.py
# Author： steam
# Time    : 2018/7/17 下午3:53

import time
import subprocess


def clean_log():
    cmd = 'rm user*.log'
    cmd_p1 = 'rm p1-user*.log'
    cmd_p2 = 'rm p2-user*.log'
    subprocess.Popen(cmd,shell=True)
    subprocess.Popen(cmd_p1,shell=True)
    subprocess.Popen(cmd_p2,shell=True)


if __name__ == '__main__':
    clean_log()
    time.sleep(3600)
