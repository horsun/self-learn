from whoosh.fields import *
from whoosh.index import create_in, open_dir
import os
from whoosh.qparser import QueryParser

# whoosh在应用上划分三个步骤：
# 1.建立索引和模式对象
# 2.写入索引文件
# 3.搜索

schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)


# or
class MySchema(SchemaClass):
    path = ID(stored=True)
    title = TEXT(stored=True)
    content = TEXT
    tags = KEYWORD
    icon = TEXT


# stored = True 表示返回结果字段


if not os.path.exists('index'):
    os.mkdir('index')
indeeex = create_in('index', MySchema)
# 用create_in创建一个具有前述索引模式的索引存储目录对象，所有的索引将被保存在该目录（index）中。
writer = indeeex.writer()
writer.add_document(title=u"my document", content=u"this is my document", path=u"/a", tags=u"firlst short",
                    icon=u"/icons/star.png")
writer.add_document(title=u"my second document", content=u"this is my second document", path=u"/b",
                    tags=u"second short", icon=u"/icons/sheep.png")
writer.commit()

# searcher = indeeex.searcher()
# 和open()类似 用with方法保持状态
with indeeex.searcher() as searcher:
    # do something
    query = QueryParser("content", indeeex.schema).parse("second")
    result = searcher.search(query)
    print(result)
    print(list(result))
