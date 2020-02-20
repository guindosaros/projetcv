import graphene
import cvapp.schema


class Query(cvapp.schema.Query, graphene.ObjectType):
  pass
  class Meta:
     description = 'Query de Mon cv en ligne'


schema = graphene.Schema(query=Query)