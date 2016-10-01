#coding=utf8
import MySQLdb

try:
    conn=MySQLdb.connect(host='192.168.18.69',user='root',passwd='niiwooroot',port=3306,charset='utf8')  #连接数据库
    conn.select_db('ubas_tianchengtest')  #选择数据库
    cur=conn.cursor()
    #conn2=MySQLdb.connect(host='192.168.18.69',user='root',passwd='niiwooroot',port=3306,charset='utf8')  #连接数据库
    #conn2.select_db('ups')  #选择数据库



    #conn.select_db('ups')
    #cur=conn.cursor()
    whwh = 1
    count = cur.execute("SELECT UserID,Title,BorrowerAmount,BorrowerRate FROM postmodifyloaneevent WHERE SourceID = %s", (whwh,))
    print 'count there has %s rows record' % count

    #cur2=conn2.cursor()
    #count2 = cur2.execute("SELECT UserID, RealName, Idcard, result, message FROM verifyrealnameevent20150907")
    #print 'count2 there has %s rows record' % count2


    #query_str = "INSERT INTO userbasicinfo(UserId,UserType,UserStatus,LoginFromOthers) VALUES(%s,%s,%s,%s)"
    #query_value = ('test12345-902a6670-73b9-11e5-80b7-b083fe6509c401', 1, 0, 'QQ')
    #cur.execute(query_str, query_value)

    #count=cur.execute("SELECT UserId FROM userbasicinfo WHERE UserId = %s", ('test12345-902a6670-73b9-11e5-80b7-b083fe6509c412',))
    #print 'there has %s rows record' % count

    result = cur.fetchone()
    print 'result type: ', type(result)
    print 'result: ',result

    #result=cur.fetchmany(2)
    #print 'result type: ', type(result)
    #print 'result: ',result

    #result=cur.fetchall()
    #print 'result type: ', type(result)
    #print 'result: ',result

    #result2=cur2.fetchone()
    #print 'result2: ',result2

    #print type(result)
    #conn.commit()
    cur.close()
    conn.close()
    #cur2.close()
    #conn2.close()


except MySQLdb.Error as e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
     raise

