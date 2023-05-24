from django.shortcuts import get_object_or_404, render
from rest_framework import status, viewsets
from user.serializers import UserSerializer
from user.models import User
from bson.objectid import ObjectId


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "_id"


    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        try:
            try:
                filter_kwargs = {"_id": ObjectId(self.kwargs[lookup_url_kwarg])}
            except:
                filter_kwargs = {"slug": self.kwargs[lookup_url_kwarg]}
            user_data = get_object_or_404(queryset, **filter_kwargs)
            self.check_object_permissions(self.request, user_data)
        except:
            message = (
                f"Inavalid request: User Not Found: {self.kwargs[self.lookup_field]}"
            )
            raise Exception({"message": ValueError(message)}, message, 400)
        return user_data