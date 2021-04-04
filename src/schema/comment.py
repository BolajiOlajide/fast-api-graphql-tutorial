import graphene

from src.serializers import CommentGrapheneInputModel, CommentGrapheneModel
from models.comment import Comment
from models.post import Post
from models.user import User


class CreateComment(graphene.Mutation):
    class Arguments:
        comment_details = CommentGrapheneInputModel()

    Output = CommentGrapheneModel

    @staticmethod
    def mutate(parent, info, comment_details):
        user = User.find_or_fail(comment_details.user_id)
        post = Post.find_or_fail(comment_details.post_id)

        comment = Comment()
        comment.body = comment_details.body

        user.comments().save(comment)
        post.comments().save(comment)

        return comment
