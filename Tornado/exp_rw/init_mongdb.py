#coding=utf8
import pymongo

conn = pymongo.MongoClient('mongodb://tataufo:Inno3pku@192.168.3.4:27017/')
db = conn.example


# db.words.insert({"word": "oarlock", "definition": "A device attached to a rowboat to hold the oars in place"})
# db.words.insert({"word": "seminomadic", "definition": "Only partially nomadic"})
# db.words.insert({"word": "perturb", "definition": "Bother, unsettle, modify"})

print 'db.collection_names: ', db.collection_names()

print db.words.find_one({"word":"oarlock"})
