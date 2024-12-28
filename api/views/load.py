from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.load.models import Load
from api.dto.load import LoadSerializer
from rest_framework import generics
class LoadListView(APIView):
    def get(self, request):
        loads = Load.objects.all()
        serializer = LoadSerializer(loads, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LoadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoadDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Load.objects.all()
    serializer_class = LoadSerializer
    # permission_classes = [permissions.IsAuthenticated]
