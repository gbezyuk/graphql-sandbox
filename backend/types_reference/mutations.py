import graphene

class CreatePerson(graphene.Mutation):
    class Input:
        name = graphene.String()

    ok = graphene.Boolean()
    person = graphene.Field(lambda: Person)

    @staticmethod
    def mutate(root, args, context, info):
        person = Person(name=args.get('name'))
        ok = True
        return CreatePerson(person=person, ok=ok)

"""
person and ok are the output fields of the Mutation when is resolved.

Input attributes are the arguments that the Mutation CreatePerson needs for resolving, in this case name will be the only argument for the mutation.

mutate is the function that will be applied once the mutation is called.
"""

class Person(graphene.ObjectType):
    name = graphene.String()
    age = graphene.Int()

class MyMutations(graphene.ObjectType):
    create_person = CreatePerson.Field()

# We must define a query for our schema
class Query(graphene.ObjectType):
    person = graphene.Field(Person)

schema = graphene.Schema(query=Query, mutation=MyMutations)

"""
Then, if we query `schema.execute(query_str)` the following:

mutation myFirstMutation {
    createPerson(name:"Peter") {
        person {
            name
        }
        ok
    }
}

We should receive:

{
    "createPerson": {
        "person" : {
            name: "Peter"
        },
        "ok": true
    }
}
"""

"""
InputFields are used in mutations to allow nested input data for mutations
To use an InputField you define an InputObjectType that specifies the structure of your input data
"""

class PersonInput(graphene.InputObjectType):
    name = graphene.String()
    age = graphene.Int()


class CreatePerson(graphene.Mutation):
    class Input:
        person_data = graphene.Argument(PersonInput)

    person = graphene.Field(lambda: Person)

    @staticmethod
    def mutate(root, args, context, info):
        p_data = args.get('person_data')

        name = p_data.get('name')
        age = p_data.get('age')

        person = Person(name=name, age=age)
        return CreatePerson(person=person)

"""
Note that name and age are part of person_data now
Using the above mutation your new query would look like this:

mutation myFirstMutation {
    createPerson(personData: {name:"Peter", age: 24}) {
        person {
            name,
            age
        }
    }
}
"""

"""
InputObjectTypes can also be fields of InputObjectTypes allowing you
to have as complex of input data as you need
"""


class LatLngInput(graphene.InputObjectType):
    lat = graphene.Float()
    lng = graphene.Float()


#A location has a latlng associated to it
class LocationInput(graphene.InputObjectType):
    name = graphene.String()
    latlng = graphene.InputField(LatLngInput)
