import pymongo


class MongoClient(object):
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://127.0.0.1:27017")

    def get_db_list(self):
        return self.client.list_database_names()

    def get_collection_list(self, db_name):
        return self.client[db_name].collection_names()

    def create_db(self, db_name):
        return self.client[db_name]

    def create_collection(self, db_name, coll_name):
        if coll_name not in self.get_collection_list(db_name):
            self.client[db_name].create_collection(coll_name)
        return self.client[db_name][coll_name]

    def insert(self, data, **kwargs):
        if isinstance(data, list):
            self.create_collection(**kwargs).insert_many(data)
        if isinstance(data, dict):
            self.create_collection(**kwargs).insert_one(data)


if __name__ == '__main__':
    client = MongoClient()
    db_list = client.get_db_list()
    print(db_list)
    collection_list = []
    for db_name in db_list:
        for x in client.get_collection_list(db_name):
            collection_list.append(x)
    coll = client.create_collection(db_name='monitor', coll_name='system_info')
    from pprint import pprint

    pprint(list(coll.find()))
