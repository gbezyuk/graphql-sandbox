"""
A Schema is created by supplying the root types of each type of operation,
query and mutation (optional).
A schema definition is then supplied to the validator and executor.
"""

# my_schema = Schema(
#    query=MyRootQuery,
#    mutation=MyRootMutation,

#    There are some cases where the schema cannot access all of the types that we plan to have.
#    In this case, we need to use the `types` argument when creating the Schema.
#    types=[SomeExtraObjectType, ]

#    By default all field and argument names (that are not explicitly set with the name arg)
#    will be converted from snake_case to camelCase (as the API is usually being consumed by
#    a js/mobile client). 
#    To disable this behavior, set the `auto_camelcase` to False upon schema instantiation.
#    auto_camelcase=False,
# )

# To query a schema, call the execute method on it.
# my_schema.execute('{ lastName }')
