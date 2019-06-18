import random
import time
from rest_framework.response import Response

from rest_framework import generics, status
from rest_framework_auth0.authentication import Auth0JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from scarface.models import Device
from scarface.exceptions import NotRegisteredException
from .tasks import send_email_upon_signup, device_register
from . import models
from . import serializers


class UserCreateView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    authentication_classes = (Auth0JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):

        # remove Tracking
        serializer = self.serializer_class(data=request.data)
        tracking_serializer = serializers.TrackingSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True) and tracking_serializer.is_valid(raise_exception=True):
            data = serializer.validated_data

            def ticket_ref_generator():
                rng = random.SystemRandom(45645 * time.time())
                ticket_ref = [str(rng.randint(0, 9)) for i in range(10)]
                ticket_ref = ''.join(ticket_ref)

                return ticket_ref

            # get the user
            user = request.user
            for attr, value in data.items():
                setattr(user, attr, value)

            user.save()
            tracking, created = tracking_serializer.get_or_create(user=user, ticket_ref=ticket_ref_generator())

            if created:
                send_email_upon_signup.delay(user.id, tracking.id)

            return Response(status=status.HTTP_204_NO_CONTENT)


class AuthNoUser(Auth0JSONWebTokenAuthentication):
    create_unknown_user = False


class UserDetailView(generics.RetrieveAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    authentication_classes = (AuthNoUser,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        # get the user
        user = request.user
        device_id = request.GET.get('device_id')
        if user:
            if device_id:
                pushes = [t.push for t in user.tracking.filter(unique_id=device_id)]
            else:
                pushes = [t.push for t in user.tracking.all()]
            if pushes:
                push = all(pushes)
            else:
                push = False

            payload = {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'mobile': user.mobile,
                'organisation': user.organisation,
                'postcode': user.postcode,
                'push': push
            }
            return Response(data=payload, status=status.HTTP_200_OK, )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class DeviceView(generics.CreateAPIView):
    serializer_class = serializers.DeviceSerializer
    authentication_classes = (AuthNoUser,)
    permission_classes = (IsAuthenticated,)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data

            try:
                tracking = request.user.tracking.get(unique_id=data['unique_id'])
            except:
                return Response(data={'error': 'Device Unique ID Not Registered'}, status=status.HTTP_400_BAD_REQUEST)

            if data['push']:
                tracking.device_token = data['device_token']
                tracking.push = True
                tracking.save()
                device_register.delay(tracking.id)

            else:
                tracking.push = False
                tracking.save()
                try:
                    device = Device.objects.get(device_id=tracking.unique_id)
                except Device.DoesNotExist:
                    return Response(data={'error': 'Device Not Registered'}, status=status.HTTP_400_BAD_REQUEST)
                try:
                    device.deregister()
                except NotRegisteredException:
                    return Response(data={'error': 'Device Not Registered'}, status=status.HTTP_400_BAD_REQUEST)

            return Response(data={'success': True, 'msg': 'Request suceeded'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
