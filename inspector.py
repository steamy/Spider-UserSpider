#!/usr/bin/python3 
# -*- coding: utf-8 -*-
# Filename:  inspector.py
# Author： steam
# Time    : 2018/7/16 下午4:47

import schedule
import subprocess
from userSpider.redis_pool import redisPool
from redis import Redis
import datetime
import time
import logging
import os

log_path = './log/watcher.log'
os.makedirs('./log')
f = open(log_path,'ab')
f.close()
LOG_FORMATE = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename=log_path, level=logging.INFO, format=LOG_FORMATE)



def watcher():

    # ip 代理池状态
    #proxy_ip_status_cmd = 'curl http://127.0.0.1:5010/get_status/'
    #proxy_ip_status = subprocess.Popen(proxy_ip_status_cmd, stdout = subprocess.PIPE, stdin = subprocess.PIPE, shell=True)
    #print('【ip_proxy_pool】' + str(datetime.datetime.now()) + str(proxy_ip_status.communicate()[0]))
    # 爬取用户数
    # r = Redis(connection_pool=redisPool)
    # print('【reids】' + str(datetime.datetime.now()) + '已经爬取'+ str(r.scard('userid_used')) + '个用户');
    # print('【reids】' + str(datetime.datetime.now()) + '还未爬取' + str(r.scard('userid_wanted')) + '个用户');

    logging.info('test')


# schedule.every(20).seconds.do(watcher)

if __name__ == '__main__':
    # schedule.run_pending()
    while True:
        watcher()
        time.sleep(20)





