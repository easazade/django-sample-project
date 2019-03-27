from django.db import models


# Create your models here.
# title
# pub_date
# body
# image

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField(blank=True)
    image = models.ImageField("blogimages/")
