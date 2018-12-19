import pymemcache
from pymemcache.client.base import Client
import json


def enJson(key, value):
    if type(value) == str:
        return value, 1
    return json.dumps(value), 2


def deJson(key, value, flags):
    if flags == 1:
        return value
    if flags == 2:
        return json.loads(value)
        # raiseException("Unknown serialization format")


client = Client(('127.0.0.1', 11211), serializer=enJson, deserializer=deJson)
client.set('name', 'jinhao2')
client.set('json', {"name": "jinhao", "age": 2})
result = client.get('name')
print(client.get('json'))
print(result)
