from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.blog.models import Post, PostCategory
from apps.blog.serializers import PostSerializer


def blog_post(request, pk):
    """
    The following renders the actual post.

    We simply find the blog post corresponding to the blog entry's date.
    :param request:
    :param pk:
    :return:
    """
    try:
        post = Post.objects.get(pk=pk)
        return render(request, 'blog/post.html', {
            'title': post.title,
            'category': PostCategory.objects.get(id=post.category_id),
            'date_added': post.date_added,
            'last_modified': post.last_modified,
            'description': post.description,
            'content': post.content,
        })

    except Post.DoesNotExist:
        raise Http404("Post does not exist")


def get_partial(request):
    """
    Returns the Foundation grid containing the blog posts.
    :param request:
    :return:
    """
    return render(request, 'blog/partials/list.html')


class PostList(APIView):
    """

    """

    def get(self, request, format=None):
        """
        Listing of blog posts written.
        :param request:
        :param format:
        :return:
        """
        posts = Post.objects.all().order_by('date_added')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

