from receiver.models import Record
from receiver.serializers import RecordSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

class RecordList(APIView):
    """
    Listing all the records, or create a new one.
    """

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        records = Record.objects.filter(owner=self.request.user)
        serializer = RecordSerializer(records, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RecordSerializer(data=request.data)
        print(serializer.initial_data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
