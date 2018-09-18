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
import json

log_path = './log/watcher.log'
if not os.path.exists('./log'):
   os.makedirs('./log')
f = open(log_path,'ab')
f.close()
LOG_FORMATE = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename=log_path, level=logging.INFO, format=LOG_FORMATE)

def watcher():
    f = open('./watcher.log','w+')
    # ip 代理池状态
    proxy_ip_status_cmd = 'curl http://127.0.0.1:5010/get_status/'
    proxy_ip_status = subprocess.Popen(proxy_ip_status_cmd, stdout = subprocess.PIPE, stdin = subprocess.PIPE, shell=True)
    logging.info('【ip_proxy_pool】'  + str(proxy_ip_status.communicate()[0]))
    # 爬取用户数
    r = Redis(connection_pool=redisPool)
    userid_used_num = r.scard('userid_used')
    userid_wanted_num = r.scard('userid_wanted')
    message = {
        'userid_used_num': userid_used_num,
        'userid_wanted_num': userid_wanted_num
    }
    logging.info('【reids】' + '已经爬取'+ str(userid_used_num) + '个用户')
    logging.info('【reids】'+ '还未爬取' + str(userid_wanted_num) + '个用户')
    r.publish('fetched_user_num_update', str(json.dumps(message)))

#schedule.every(10).minutes.do(watcher)

if __name__ == '__main__':
    while True:
       #schedule.run_pending()
       r = Redis(connection_pool=redisPool)
       refresh_interval  =  r.get('spider_monitor_refresh_time')
       watcher()
       print("refresh_interval!!!:")
       print(refresh_interval)
       time.sleep(int(refresh_interval) * 60)
