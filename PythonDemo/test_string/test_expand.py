#coding=utf8
"""
替换字符串中的子串
"""

def expand(s, d, mark='"', safe=False):
    if safe:
        def lookup(w):
            # print 'w: ',w
            # print 'mark*2', mark*2
            # print 'w.join(mark*2)', w.join(mark*2)
            return d.get(w, w.join(mark*2))
    else:
        def lookup(w):
            return d.get(w)

    parts = s.split(mark)
    parts[1::2] = map(lookup, parts[1::2])
    return ''.join(parts)

print expand('sdfsdf sdfsdd"thing"sjdjfdsjfoisdf ',{'thingd':'milk'},safe=True)
