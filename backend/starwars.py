import graphene

class Episode(graphene.Enum):
    NEWHOPE = 4
    EMPIRE = 5
    JEDI = 6

    @property
    def description(self):
        if self == Episode.NEWHOPE:
            return 'New Hope Episode'
        return 'Other episode'

# Alternative syntax is as follows:
# Episode = graphene.Enum('Episode', [('NEWHOPE', 4), ('EMPIRE', 5), ('JEDI', 6)])
#
# One can use python enums too:
# graphene.Enum.from_enum(AlreadyExistingPyEnum)
# (see https://docs.python.org/3/library/enum.html)
#
# Actually, as official docs say, quote:
# "graphene.Enum uses enum.Enum internally (or a backport if that’s not available)
# and can be used in the exact same way.
# (see http://docs.graphene-python.org/en/latest/types/enums/)

