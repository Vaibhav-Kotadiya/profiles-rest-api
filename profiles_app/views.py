from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_app.serializers import HelloSerializer, UserProfileSerializer
from profiles_app.models import UserProfile
from profiles_app.permissions import UpdateOwnProfile


class HelloApiView(APIView):
    serializer_class = HelloSerializer

    def get(self, request, format=None):
        list = ['Hello','World']

        return Response(
        {'message': 'Hey!', 'list': list}
        )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        return Response(serializer.errors,
                        status = status.HTTP_400_BAD_REQUEST
                        )

    def put(self, request, pk=None):
        return Response({'message': 'PUT'})

    def patch(self, request, pk=None):
        return Response({'message': 'PATCH'})

    def delete(self, request):
        return Response({'message': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):

    serializer_class = HelloSerializer

    def list(self, request):
        a_viewlist = [
        'Uses action (list, create, retrieve, update, partial_update)',
        'Automatically maps to URLs using Routers.',
        'Provides more functionality with less code.'
        ]

        return Response({'message': 'Hello!', 'a_viewlist': a_viewlist})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})

        return Response(
        serializer.errors,
        status = status.HTTP_400_BAD_REQUEST
        )

    def retrieve(self, request, pk=None):
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle in creating and updating user profiles."""

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email', )


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication token"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
