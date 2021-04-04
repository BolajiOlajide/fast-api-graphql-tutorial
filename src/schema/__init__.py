import graphene

from .user import CreateUser
from .post import CreatePost
from .comment import CreateComment
from src.serializers import UserGrapheneModel
from models.user import User


class Query(graphene.ObjectType):
    say_hello = graphene.String(name=graphene.String(default_value="Hello World!"))
    list_users = graphene.List(UserGrapheneModel)
    get_single_user = graphene.Field(
        UserGrapheneModel, user_id=graphene.NonNull(graphene.Int)
    )

    @staticmethod
    def resolve_say_hello(parent, info, name):
        return f"Hello {name}"

    @staticmethod
    def resolve_list_users(parent, info):
        return User.all()

    @staticmethod
    def resolve_get_single_user(parent, info, user_id):
        return User.find_or_fail(user_id)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_post = CreatePost.Field()
    create_comment = CreateComment.Field()
