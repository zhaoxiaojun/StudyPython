#coding=utf8
from locust import Locust, TaskSet, task


class MyTaskSet(TaskSet):
    @task(1)
    class SubTaskSet(TaskSet):
        @task
        def my_task1(self):
            print 'my_task1'

        @task
        def my_task2(self):
            print 'my_task2'

    @task(10)
    def yo_task(self):
        print 'yo_task'



class MyLocust(Locust):
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 1000
