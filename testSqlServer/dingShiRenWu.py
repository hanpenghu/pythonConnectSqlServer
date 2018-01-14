# -*- coding: UTF-8 -*-
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

def my_job():
    print('hello world')


sched = BlockingScheduler()
sched.add_job(my_job, 'interval', seconds=1)
sched.start()