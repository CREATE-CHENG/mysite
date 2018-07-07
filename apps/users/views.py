from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from rest_framework_jwt.settings import api_settings


class SocialToJwtView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(request.user)
        token = jwt_encode_handler(payload)
        return Response({'token': token})

