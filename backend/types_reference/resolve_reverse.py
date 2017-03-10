import graphene


def reverse(root, args, context, info):
    word = args.get('word')
    return word[::-1]


class Query(graphene.ObjectType):
    reverse = graphene.String(word=graphene.String(), resolver=reverse)
