import schedule
import time
import datetime

# from apscheduler.events import EVENT_ALL, EVENT_JOB_EXECUTED
#
#
from apscheduler.events import EVENT_JOB_EXECUTED


class Counter():
    count = 0

    def inc(self):
        self.count = self.count + 1

    def get(self):
        return self.count

#
# def job():
#
#     print("I'm working...", datetime.datetime.now())
#     print(len(schedule.jobs))
#     time.sleep(5)
#     print("done working...", datetime.datetime.now())
#
# max = 3
#
#
# from apscheduler.schedulers.background import BackgroundScheduler
#
#
#
# def some_job(counter):
#     counter.inc()
#     print('start', datetime.datetime.now())
#     time.sleep(5)
#     print('done', datetime.datetime.now())
#
#
# # seconds can be replaced with minutes, hours, or days
#
#
# counter = Counter()
#
#
# while counter.get() < max:
#     time.sleep(1)


#sched.shutdown()
from apscheduler.schedulers.background import BackgroundScheduler


class ScheduledTask():

    def my_listener(self, mevent):
        #print(str(mevent))
        print('listner: ', datetime.datetime.now(), str(self.counter.get()))
        self.counter.inc()
        if(self.counter.get() >= self.maxIterations):
            print('calling shutdown: ', str(datetime.datetime.now()))
            self.sched.shutdown()

    def __init__(self, maxIterations):
        self.sched = BackgroundScheduler()
        self.counter = Counter()
        self.maxIterations = maxIterations
        self.sched.add_listener(self.my_listener, EVENT_JOB_EXECUTED)

    def runTask(self, job, interval, args):
        self.sched.add_job(job, 'interval', seconds=interval, max_instances=100, args=args)
        self.sched.start()

    def isDone(self):
        if self.counter.get() < self.maxIterations:
            print('not dont yet')
            return False
        else:
            print('done')
            return True

# sc = ScheduledTask(40)
# sc.runTask(func, 1.5)
#
# while sc.isDone() == False:
#     time.sleep(1)

