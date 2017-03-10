import graphene

class UserFields(graphene.AbstractType):
    name = graphene.String()

class User(graphene.ObjectType, UserFields):
    pass

class UserInput(graphene.InputObjectType, UserFields):
    pass

"""
The above types have the following representation in a schema:

type User {
  name: String
}

inputtype UserInput {
  name: String
}
"""
