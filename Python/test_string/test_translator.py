#coding=utf8
import string
import sets

#对translate的一层包装
def translator(frm='', to='', delete='', keep=None):
    if len(to)==1:
        to = to*len(frm)

    trans = string.maketrans(frm, to)
    if keep is not None:
        allchars = string.maketrans('','') #一个无需翻译的翻译表
        delete = allchars.translate(allchars, keep.translate(allchars, delete))

    def translate(s):
        return s.translate(trans, delete)
    return translate


digits_only = translator(keep=string.digits)
print digits_only('CHsds persdks: 2234-2345')

digits_to_hash = translator(frm=string.digits, to='#')
print digits_to_hash('CHsds persdks: 2234-2345')




#对translate的一层包装：过滤
def makefilter(keep):
    allchars = string.maketrans('','')
    #  print 'allchars: ', allchars
    delchars = allchars.translate(allchars, keep)

    def thefilter(s):
        return s.translate(allchars, delchars)
    return thefilter

just = makefilter('aeiouy ')
print just('four score and seven years ago')



#去重、字典序
s = 'nvjsdfoasdsd  u hfks '
allchars = string.maketrans('','')
ss = makefilter(s)(allchars)
print ss


#适用于含unicode字符的字符串
class Keeper(object):
    def __init__(self, keep):
        self.keep = sets.Set(map(ord, keep))

    def __getitem__(self, n):
        if n not in self.keep:
            return None
        return unichr(n)

    def __call__(self, s):
        return unicode(s).translate(self)

uncmakefilter = Keeper
justu = uncmakefilter('aeiouy')
print justu(u'four 阿e萨e德 sdds yreas e以前e')
