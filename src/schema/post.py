import graphene

from src.serializers import PostGrapheneInputModel, PostGrapheneModel
from models.post import Post
from models.user import User


class CreatePost(graphene.Mutation):
    class Arguments:
        post_details = PostGrapheneInputModel()

    Output = PostGrapheneModel

    @staticmethod
    def mutate(parent, info, post_details):
        user = User.find_or_fail(post_details.user_id)
        post = Post()
        post.title = post_details.title
        post.body = post_details.body

        user.posts().save(post)

        return post
