class Person(graphene.ObjectType):
    name = graphene.String()

# Is equivalent to:
# class Person(graphene.ObjectType):
#     name = graphene.Field(graphene.String)
