from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from quickstart.serializers import UserSerializer, GroupSerializer, AuthResponseSerializer
from drf_spectacular import utils


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


# Create your views here.
class CustomAuthToken(ObtainAuthToken):
    @utils.extend_schema(
        responses={
            (200, 'application/json'): utils.OpenApiResponse(response=AuthResponseSerializer)
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(AuthResponseSerializer({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'groups': user.groups
        }).data)
