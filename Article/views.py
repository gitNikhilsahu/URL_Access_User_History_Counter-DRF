from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .models import Article
from .serializers import UserSerializer, ArticleSerializer

from History.mixins import ObjectViewMixin

# from rest_framework.decorators import api_view, renderer_classes
# from rest_framework.renderers import JSONRenderer

# @api_view(['GET'])
# @renderer_classes([JSONRenderer])
# def user_count_view(request, format=None):
#     """
#     A view that returns the count of active users in JSON.
#     """
#     user_count = User.objects.filter(active=True).count()
#     content = {'user_count': user_count}
#     return Response(content)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class ArticleViewSet(ObjectViewMixin, viewsets.ModelViewSet):
    model = Article
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAuthenticated,)