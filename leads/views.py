from rest_framework import generics
from rest_framework_auth0.authentication import Auth0JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.reverse import reverse
from rest_framework.views import APIView

from . import serializers
from . import models


class AuthNoUser(Auth0JSONWebTokenAuthentication):
    create_unknown_user = False


class LeadCreateView(generics.CreateAPIView):
    queryset = models.LeadDB.objects.all()
    serializer_class = serializers.LeadSerializer
    authentication_classes = (AuthNoUser,)
    permission_classes = (IsAuthenticated,)
