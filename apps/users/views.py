from rest_framework import status
from rest_framework import permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from .serializers import RegisterSerializers
from ..common.renders import ResponseRender

# Create your views here.
class RegisterUserView(GenericViewSet):
    serializer_class = RegisterSerializers
    permission_classes = [permissions.AllowAny]
    renderer_classes = [ResponseRender]
    
    def post(self, request):
        serializers = RegisterSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            #TODO: send mail active
            return Response(ResponseRender.render(self, serializers.data), status=status.HTTP_201_CREATED)
        return Response(ResponseRender.render(self, serializers.errors), status=status.HTTP_400_BAD_REQUEST)