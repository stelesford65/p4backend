from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from apps.pictures.views import SingleBlogEntryPicture, PicturesViewSet, Blog_entryViewSet, BlogEntryPicture

router = routers.DefaultRouter()
router.register('blog_entry', Blog_entryViewSet, basename='blog_entry')
router.register('pictures', PicturesViewSet, basename='pictures')

custom_urlpatterns = [
    url(r'blog_entry/(?P<category_pk>\d+)/pictures$', BlogEntryPicture.as_view(), name='category_recipes'),
    url(r'blog_entry/(?P<category_pk>\d+)/pictures/(?P<pk>\d+)$', SingleBlogEntryPicture.as_view(), name='single_category_recipe'),
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns

# urlpatterns = [
#    path('', include(router.urls))
#     ]