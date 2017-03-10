# class Person(graphene.ObjectType):
#     name = graphene.String()
# Is equivalent to:
# class Person(graphene.ObjectType):
#     name = graphene.Field(graphene.String)

# graphene.Field(graphene.String, to=graphene.String())
# Is equivalent to:
# graphene.Field(graphene.String, to=graphene.Argument(graphene.String))
