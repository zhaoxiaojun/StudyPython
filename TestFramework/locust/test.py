#coding=utf8
from locust import HttpLocust, TaskSet, task

class mytest(TaskSet):
     # def on_start(self):
     #    self.client.post("/login", {
     #        "username": "test_user",
     #        "password": ""
     #    })


    @task(weight=1)   #task装饰器类似于LR中的事务，可以做嵌套。 weight相当于权重
    def transaction_1(self):
        with self.client.get(name='test1', url='/reverse/abcde', catch_response=True, headers={'cmdid':'1234'}) as response:
            #print response.content
            if 'edcba' in response.content:
                response.success()
            else:
                response.failure('error')
        print response.content

    # @task(weight=1)
    # def transaction_2(self):
    #     dt = {
    #         'parm1': '123',
    #         'parm2': 'abc'
    #     }

    #     with self.client.post(name='post', url='/transaction_2', data=dt, catch_response=True) as response:
    #         if 'yyy' in response.content:
    #             response.success()
    #         else:
    #             response.failure('error')


class myrun(HttpLocust):  #主类继承HttpLocust，用于测试http协议
    task_set = mytest
    host = 'http://qa.tataufo.com:8000'
    #min_wait = 1  #min_wait和max_wait用于设置执行task过程中的等待时间(ms，默认为1000ms)，相当于LR中Pacing的设置
    #max_wait = 1
