import graphene

import api.schema


class Query(api.schema.Query, graphene.ObjectType):
    """ This class will inherit from multiple Queries """
    pass


class Mutation(api.schema.Mutation, graphene.ObjectType):
    """ This class will inherit from multiple Queries """
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
