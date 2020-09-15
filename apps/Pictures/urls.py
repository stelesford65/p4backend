# this allows to create URLs for our app
from django.urls import path, include
# this allows to create the routes /categories /some_other_url
from rest_framework import routers
from p4backend.apps.pictures.views import PictureViewSet
router = routers.DefaultRouter()

router.register('pictures', PictureViewSet, basename='pictures')

urlpatterns = [
   path('', include(router.urls))
]