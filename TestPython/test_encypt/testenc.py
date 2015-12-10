#coding=utf8
import base64


def getde_base64(encrypted):
    '''
    base64解密
    '''
    data = base64.b64decode(encrypted)
    return data




if __name__ == '__main__':
    resultJson = '''eyJNZXNzZ2UiOiLnlKjmiLflubTpvoTkuI3nrKblkIjopoHmsYIiLCJNc2dCb2R5Ijp7IkJBSV9S
    T05HIjoiIiwiQkxBQ0tMSVNUX0FSUkFZIjoiIiwiTEFPX05BSSI6IiIsIlFIUEYiOiIiLCJRSFpY
    IjoiIiwiVE9OR19EVU5fSksiOiIiLCJaSElfTUEiOiIiLCJwbGF0Zm9ybXMiOlt7InBsYXRmb3Jt
    TmFtZSI6IlpISV9NQSIsInBsYXRmb3JtTmFtZUV4cGxhaW4iOiIg6Iqd6bq75L+h55SoIn0seyJw
    bGF0Zm9ybU5hbWUiOiJCTEFDS0xJU1RfQVJSQVkiLCJwbGF0Zm9ybU5hbWVFeHBsYWluIjoiIOe9
    kei0t+m7keWQjeWNlSJ9LHsicGxhdGZvcm1OYW1lIjoiUUhaWCIsInBsYXRmb3JtTmFtZUV4cGxh
    aW4iOiIg5YmN5rW36buR5ZCN5Y2VIn0seyJwbGF0Zm9ybU5hbWUiOiJUT05HX0RVTl9KSyIsInBs
    YXRmb3JtTmFtZUV4cGxhaW4iOiIg5ZCM55u+In1dfSwiU3RhdHVzIjoiMCIsIm1vZGVsX1Jlc3Vs
    dCI6IjEifQo='''

    ReqJson = '''eyJDdXJyZW50VGltZSI6IjIwMTUwNzIzMjAzMjEyMDAwMDAwIiwiRnVuY3Rpb25Db2RlIjoiMTAw
    MTIyIiwiTXNnQm9keSI6eyJQcm9qZWN0SWQiOiIxMjMiLCJSRUxBVElPTl9WRVJJRklDQVRJT04i
    Olt7InJlbGF0aW9uX25hbWUiOiLpmYjliJozIiwicmVsYXRpb25fcGhvbmUiOiIxODY3NTU1OTc1
    MCJ9LHsicmVsYXRpb25fbmFtZSI6IiIsInJlbGF0aW9uX3Bob25lIjoiIn1dLCJVbmlxdWVJRCI6
    ImFiYzEyMzQ1NjE1MDgzMDk3MzA4MDY4ODg1MSIsImFjY291bnRfbG9naW4iOiJ0ZXN0MTIzIiwi
    YXBwbHlEYXRlIjoiMjAxNS0wOC0wMSIsImFzc3VyZVR5cGUiOiJEIiwiYmFua19jYXJ0IjoiMTIz
    NDUiLCJibGFja0JveCI6IjEyMyIsImNyZWRpdEFkZHJlc3MiOiLljJfkuqwiLCJjdXJyZW5jeSI6
    IjIzMjMyIiwiZGVncmVlIjoi5pys56eRIiwiaWRlbnRpdHlfY2FyZCI6IjAwMzAwMTE5NTkwMTE2
    MDAzMSIsImlkdHlwZSI6IjAiLCJpcCI6IjE5Mi4xNjguMS4xMjIiLCJpc19maXJzdF90aW1lIjow
    LCJpc19zdHVkZW50IjoxLCJsb2FuTW9uZXkiOjEwMDAwLCJsb2FuVGltZUxpbWl0IjoxMiwibG9h
    blR5cGUiOiI5OSIsIm1vYmlsZV9waG9uZSI6IjE4Njc1NTU5NzUwIiwibmFtZSI6IumZiOWImiIs
    InJlYXNvbm5vIjoiMDQiLCJ1c2VyX2lkIjoiYWJjMTIzNDU2In19Cg=='''

    resultJson = getde_base64(resultJson)
    print resultJson

    ReqJson = getde_base64(ReqJson)
    print ReqJson

    data = '''ewogICAgIm92ZXJkdWVDcmVkaXRjYXJkTnVtIjogIjEiLAogICAgIm92ZXJkdWhvdXNlTG9hbiI6ICIxIiwKICAgICJvdmVyZHVlb3RoZXJMb2FuIjogIjEiCn0='''
    data = getde_base64(data)
    print data
