from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.sample.models import Sample
from apps.sample.serializers import SampleSerializer

class SampleList(APIView):

    def get(self, request, format=None):
        """
        Listing of samples in database
        """
        samples = Sample.objects.all()
        serializer = SampleSerializer(samples, many=True)
        return Response(serializer.data)

    @staticmethod
    def get_partial(request):
        """
        Returns Zurb Foundation grid containing samples
        """
        return render(request, 'sample/partials/list.html')
