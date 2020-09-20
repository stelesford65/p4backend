from pictures.models import Pictures, Blog_entry
from rest_framework import generics
from rest_framework.exceptions import (
   ValidationError, PermissionDenied
)
from rest_framework_simplejwt import authentication
from rest_framework.permissions import IsAuthenticated
# this allows us to do all the CRUD
from rest_framework import viewsets
# this is for HTTP status
# this allows to write and read data from our DB
from pictures.serializers import PictureSerializer


# we need this to send out the object (data) to the user
# Create your views here.


class Blog_entryViewSet(viewsets.ModelViewSet):
   permission_classes = (IsAuthenticated,)
   def get_queryset(self):
      # list  categories per current loggedin user
      queryset = Blog_entry.objects.all().filter(owner=self.request.user)
      return queryset
   serializer_class = PictureSerializer
   def create(self, request, *args, **kwargs):
      # check if category already exists for current logged in user
      blog_entry = Blog_entry.objects.filter(
         title=request.data.get('title'),
         owner=request.user
      )
      if blog_entry:
         msg = 'blog_entry with that title already exists'
         raise ValidationError(msg)
      return super().create(request)
   def perform_create(self, serializer):
      serializer.save(owner=self.request.user)
   # user can only delete category he created
   def destroy(self, request, *args, **kwargs):
      blog_entry = Blog_entry.objects.get(pk=self.kwargs["pk"])
      if not request.user == blog_entry.owner:
         raise PermissionDenied("You can not delete this blog entry")
      return super().destroy(request, *args, **kwargs)

class BlogEntryPicture(generics.ListCreateAPIView):
   permission_classes = (IsAuthenticated,)
   def get_queryset(self):
      if self.kwargs.get("blog_entry_pk"):
         blog_entry = Blog_entry.objects.get(pk=self.kwargs["blog_entry_pk"])
         queryset = Pictures.objects.filter(
            owner=self.request.user,
            blog_entry=blog_entry
         )
         return queryset
      serializer_class = PictureSerializer
   def perform_create(self, serializer):
      serializer.save(owner=self.request.user)

class SingleBlogEntryPicture(generics.RetrieveUpdateDestroyAPIView):
   permission_classes = (IsAuthenticated,)
   serializer_class = PictureSerializer
   def get_queryset(self):
      # localhost:8000/categories/category_pk<1>/recipes/pk<1>/
      """
      kwargs = {
         "blog_entry_pk": 1,
         "pk": 1
      }
      """
      if self.kwargs.get("blog_entry_pk") and self.kwargs.get("pk"):
         blog_entry = Blog_entry.objects.get(pk=self.kwargs["blog_entry_pk"])
         queryset = Pictures.objects.filter(
            pk=self.kwargs["pk"],
            owner=self.request.user,
            blog_entry=blog_entry)
         return queryset

class PicturesViewSet(viewsets.ModelViewSet):
   permission_classes = (IsAuthenticated,)
   serializer_class = PictureSerializer
   def get_queryset(self):
      queryset = Pictures.objects.all().filter(owner=self.request.user)
      return queryset
   def create(self, request, *args, **kwargs):
      if request.user.is_anonymous:
         raise PermissionDenied(
            "Only logged in users with accounts can upload a picture"
         )
      return super().create(request, *args, **kwargs)
   def perform_create(self, serializer):
      serializer.save(owner=self.request.user)
   def destroy(self, request, *args, **kwargs):
      pictures = Pictures.objects.get(pk=self.kwargs["pk"])
      if not request.user == pictures.owner:
         raise PermissionDenied(
            "You have no permissions to delete this picture"
         )
      return super().destroy(request, *args, **kwargs)
   def update(self, request, *args, **kwargs):
      pictures = Pictures.objects.get(pk=self.kwargs["pk"])
      if not request.user == pictures.owner:
         raise PermissionDenied(
            "You have no permissions to edit this picture"
         )
      return super().update(request, *args, **kwargs)


