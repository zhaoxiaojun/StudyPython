#coding=utf8
import getopt
"""
getopt模块是专门用来处理命令行参数的
函数: getopt(args, shortopts, longopts = [])
参数: args一般是sys.argv[1:]   shortopts  短格式 (-)    longopts 长格式(--)

"hp:i:"
短格式: h 后面没有冒号：表示后面不带参数，p：和 i：后面有冒号表示后面需要参数

["help","ip=","port="]
长格式: help后面没有等号=，表示后面不带参数，其他三个有=，表示后面需要参数

options,args = getopt.getopt(sys.argv[1:],"hp:i:",["help","ip=","port="])
返回值: options是个包含元祖的列表，每个元祖是分析出来的格式信息，比如 [('-i','127.0.0.1'),('-p','80')] ;
        args是个列表，包含那些没有‘-’或‘--’的参数，比如：['55','66']

注意：定义命令行参数时，要先定义带'-'选项的参数，再定义没有‘-’的参数
"""
def usage():
        print 'usage: '
        print sys.argv[0] + ' -h host/ip -p port -c functioncode -f datafile'
        print sys.argv[0] + ' --host=host/ip --port=port  --code=functioncode  --file=datafile'
        print sys.argv[0] + ' --help'

if __name__ == '__main__':
    num_args = len(sys.argv) - 1
    #获取命令行参数
    if num_args != 0:
        opts, args = getopt.getopt(sys.argv[1:], "h:p:c:f:", ["help", "host=", "port=", "code=", "file="])
        for op, value in opts:
            if (op=='-h') or (op=='--input'):
                host = value
            elif (op=='-p') or (op=='--port'):
                port = value
            elif (op=='-c') or (op=='--code'):
                functioncode = value
            elif (op=='-f') or (op=='--file'):
                datafile = value
            elif op=='--help':
                usage()
                sys.exit()
        print "host port functioncode datafile: ",host,port,functioncode,datafile
