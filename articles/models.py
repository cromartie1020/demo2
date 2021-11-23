from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to='media', default='default.jpg', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50]+'...'
