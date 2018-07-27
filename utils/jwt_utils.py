from users.serializers import UserSerializer


def jwt_response_payload_handler(token, user=None, permission=0, request=None):
    if permission:
        return {
            'token': token,
            'user': UserSerializer(user, context={'request': request}).data,
            'permission': 1
        }
    else:
        return {
            'token': token,
            'user': UserSerializer(user, context={'request': request}).data
        }