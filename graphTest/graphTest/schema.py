import graphene

import book.schema


class Query(
    book.schema.Query,
    graphene.ObjectType):
    # 总的Schema的query入口
    pass


class Mutations(graphene.ObjectType):
    # 总的Schema的mutations入口
    create_book = book.schema.CreateBook.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
