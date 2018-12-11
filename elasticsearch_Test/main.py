from elasticsearch import Elasticsearch
from mongoTest.MongoClient_TEST import MongoClient

# es = Elasticsearch()
# result = es.indices.create(index='news', ignore=400)
# print(result)
print(list(MongoClient().create_collection(db_name='monitor', coll_name='system_info').find()))
