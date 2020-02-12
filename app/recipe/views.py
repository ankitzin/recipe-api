from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag
from recipe import serializers


<<<<<<< HEAD
class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
=======
class TagViewSet(viewsets.GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin):
>>>>>>> master
    """Manage Tags in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer

    def get_queryset(self):
        """return objects for the current authentication user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')
<<<<<<< HEAD
=======

    def perform_create(self, serializer):
        """Create a new Tag"""
        serializer.save(user=self.request.user)
>>>>>>> master
