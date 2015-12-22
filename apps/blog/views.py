from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.blog.models import Post
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
            'img_src': post.img_src,
            'description': post.description,
            'date': post.date,
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
        posts = Post.objects.all().order_by('date')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

