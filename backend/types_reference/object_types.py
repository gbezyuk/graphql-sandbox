import graphene


class Person(graphene.ObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    full_name = graphene.String()

    def resolve_full_name(self, args, context, info):
        return '{} {}'.format(self.first_name, self.last_name)

#   there's a way to trick auto_camelcase locally, BTW — use `name`
#   other_name = graphene.String(name='_other_Name') 


"""
`first_name` and `last_name` are fields of the `ObjectType`.
Each field is specified as a class attribute, and each attribute maps to a Field.

The above `Person` ObjectType has the following schema representation:

type Person {
  firstName: String
  lastName: String
  fullName: String
}

Graphene ObjectTypes can act as containers too. So with the previous example you could do:

peter = Person(first_name='Peter', last_name='Griffin')

peter.first_name # prints "Peter"
peter.last_name # prints "Griffin"
"""
