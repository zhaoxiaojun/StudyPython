#coding=utf8
import json



datazu = u'{"keyy1":{"水电费sdsdg中文": "水电费sdsdg中文"}, "keyy2":{"水电费sdsdg中文": "水电费sdsdg中文"}}'
print 'datazu: ',datazu
print 'type of datazu: ', type(datazu)
print '\n----------------'

datazu1 = json.loads(datazu)
print 'datazu1: ',datazu1
print 'type of datazu1: ', type(datazu1)

datazu1 = datazu1["keyy1"]
print 'datazu1: ',datazu1
print 'type of datazu1: ', type(datazu1)

datazu2 = json.dumps(datazu1, ensure_ascii=False)
print 'datazu2: ',datazu2
print 'type of datazu2: ', type(datazu2)

