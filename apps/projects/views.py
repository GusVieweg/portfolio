from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.projects.models import Project
from apps.projects.serializers import ProjectSerializer


class ProjectList(APIView):

    def get(self, request, format=None):
        """
        Listing of projects currently worked on.
        :param request:
        :param format:
        :return:
        """
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    @staticmethod
    def get_partial(request):
        """
        Returns the Foundation grid containing the projects
        :param request:
        :return:
        """
        return render(request, 'projects/partials/list.html')