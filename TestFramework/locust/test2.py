#coding=utf8
from locust import Locust, TaskSet, task

class ForumPage(TaskSet):
    @task(2)
    def read_thread(self):
        print 'read_thread'

    @task(1)
    def new_thread(self):
        print 'new_thread'

    # @task(5)
    # def stop(self):
    #     self.interrupt()


class UserBehaviour(TaskSet):
    tasks = {ForumPage:10}

    @task
    def index(self):
        print 'index'


class MyLocust(Locust):
    task_set = UserBehaviour
    min_wait = 1000
    max_wait = 1000



