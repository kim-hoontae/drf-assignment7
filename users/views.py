from rest_framework.generics    import CreateAPIView
from rest_framework.permissions import AllowAny

from users.models      import User
from users.serializers import SignupSerializers


class SignupViewSet(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = SignupSerializers
