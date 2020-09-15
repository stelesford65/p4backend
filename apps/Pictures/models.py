from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Pictures(models.Model):
    models.ImageField(upload_to='images/')
    description = models.CharField(max_length=300)
    created_by = models.IntegerField()

    def __str__(self):
        return self.title
