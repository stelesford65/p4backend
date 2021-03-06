from django.conf.urls import url
from rest_framework import routers
from pictures.views import SingleBlogEntryPicture, PicturesViewSet, Blog_entryViewSet, BlogEntryPicture

router = routers.DefaultRouter()
router.register('blog_entry', Blog_entryViewSet, basename='blog_entry')
router.register('pictures', PicturesViewSet, basename='pictures')

custom_urlpatterns = [
    url(r'blog_entry/(?P<blog_entry_pk>\d+)/pictures$', BlogEntryPicture.as_view(), name='blogentrypicture'),
    url(r'blog_entry/(?P<blog_entry_pk>\d+)/pictures/(?P<pk>\d+)$', SingleBlogEntryPicture.as_view(), name='singleblogentrypicture'),
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns

# urlpatterns = [
#    path('', include(router.urls))
#     ]