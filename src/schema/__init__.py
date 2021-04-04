import graphene

from .user import CreateUser
from .post import CreatePost
from .comment import CreateComment


class Query(graphene.ObjectType):
    say_hello = graphene.String(name=graphene.String(default_value='Hello World!'))

    @staticmethod
    def resolve_say_hello(parent, info, name):
        return f'Hello {name}'


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_post = CreatePost.Field()
    create_comment = CreateComment.Field()
