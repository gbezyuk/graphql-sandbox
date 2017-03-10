import graphene

class Character(graphene.Interface):
    name = graphene.String()

# Human is a Character implementation
class Human(graphene.ObjectType):
    class Meta:
        interfaces = (Character, )

    born_in = graphene.String()

# Droid is a Character implementation
class Droid(graphene.ObjectType):
    class Meta:
        interfaces = (Character, )

    function = graphene.String()

"""
The above types have the following representation in a schema:

interface Character {
  name: String
}

type Droid implements Character {
  name: String
  function: String
}

type Human implements Character {
  name: String
  bornIn: String
}
"""
