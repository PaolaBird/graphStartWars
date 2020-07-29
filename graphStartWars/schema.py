import graphene

import character.schema


class Query(character.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
