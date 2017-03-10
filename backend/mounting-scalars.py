class Person(graphene.ObjectType):
    name = graphene.String()

#   Is equivalent to:
#   name = graphene.Field(graphene.String)

# graphene.Field(graphene.String, to=graphene.String())
# Is equivalent to:
# graphene.Field(graphene.String, to=graphene.Argument(graphene.String))
# (Argument?) @gbezyuk


class Character(graphene.ObjectType):
    
    name = graphene.String(required=True)

#   Is equivalent to:
#   name = graphene.NonNull(graphene.String)
