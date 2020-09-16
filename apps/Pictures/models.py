from django.db import models

# Create your models here.
from django.db import models
from apps.authentication.models import User
# Create your models here.
class Blog_entry(models.Model):
   class Meta:
      verbose_name_plural = 'blog_entry'
   title = models.CharField(max_length=100)
   owner = models.ForeignKey(User, on_delete=models.CASCADE)
   description = models.TextField(blank=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   def __str__(self):
      return self.title

class Pictures(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    image_url = models.IntegerField()

    def __str__(self):
        return self.image
