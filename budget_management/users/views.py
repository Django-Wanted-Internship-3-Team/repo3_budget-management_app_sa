from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from budget_management.users.services import UserService


class SignupView(APIView):
    permission_classes = [AllowAny]

    class InputSerializer(serializers.Serializer):
        username = serializers.CharField()
        password = serializers.CharField()

    class OuputSerializer(serializers.Serializer):
        username = serializers.CharField()

    @swagger_auto_schema(
        request_body=InputSerializer,
        responses={
            status.HTTP_201_CREATED: OuputSerializer,
        },
    )
    def post(self, request):
        """
        계정명과 비밀번호를 받아서 새로운 유저를 생성합니다.

        url: /api/users/signup
        """
        user_service = UserService()
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = user_service.create(**serializer.validated_data)
        return Response(self.OuputSerializer(user).data, status=status.HTTP_201_CREATED)
