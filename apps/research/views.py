from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.research.models import Research
from apps.research.serializers import ResearchSerializer


def research_post(request, pk):
    """
    The following renders the actual post.

    We simply find the blog post corresponding to the blog entry's date.
    :param request:
    :param pk:
    :return:
    """
    try:
        post = Research.objects.get(pk=pk)
        return render(request, post.content_url, {
            'title': post.title,
            'date_added': post.date_added,
            'last_modified': post.last_modified,
            'description': post.description,
        })

    except Research.DoesNotExist:
        raise Http404("Research post does not exist")


def get_partial(request):
    """
    Returns the Foundation grid containing the projects
    :param request:
    :return:
    """
    return render(request, 'research/partials/list.html')


class ResearchList(APIView):
    """

    """

    def get(self, request, format=None):
        """
        Listing of projects currently worked on.
        :param request:
        :param format:
        :return:
        """
        posts = Research.objects.all().order_by('-date_added')
        serializer = ResearchSerializer(posts, many=True)
        return Response(serializer.data)
