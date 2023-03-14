from rest_framework import status
from rest_framework import permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from .serializers import RegisterSerializers

# Create your views here.
class RegisterUserView(GenericViewSet):
    serializer_class = RegisterSerializers
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request):
        serializers = RegisterSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)