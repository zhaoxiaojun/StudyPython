#coding=utf8
from locust import Locust, TaskSet, task

class MyTaskSet(TaskSet):
    data = None

    def on_start(self):  #每个用户执行1次
        print 'on_start'


    @task
    def my_task(self):
        print self.data

class MyLocust(Locust):
    task_set = MyTaskSet
    task_set.data = 'wwwwwwwwwwww'
    min_wait = 1000
    max_wait = 5000
