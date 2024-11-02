from django.utils.deprecation import MiddlewareMixin
from rest_framework.response import Response
from rest_framework import status
from .models import BlacklistedToken


class JWTBlacklistMiddleware(MiddlewareMixin):
    def process_request(self, request):
        auth = request.META.get('HTTP_AUTHORIZATION', None)
        if auth is not None:
            token = auth.split()[1]
            # Проверяем, находится ли токен в черном списке
            if BlacklistedToken.objects.filter(token=token).exists():
                return Response({"detail": "Token has been blacklisted."}, status=status.HTTP_401_UNAUTHORIZED)
