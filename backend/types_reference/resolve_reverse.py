import graphene


class Query(graphene.ObjectType):
    reverse = graphene.String(word=graphene.String())

    def resolve_reverse(self, args, context, info):
        word = args.get('word')
        return word[::-1]
