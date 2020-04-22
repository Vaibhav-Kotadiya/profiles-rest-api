from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    def get(self, request, format=None):
        list = ['Hello','World']

        return Response(
        {'message': 'Hey!', 'list': list}
        )
