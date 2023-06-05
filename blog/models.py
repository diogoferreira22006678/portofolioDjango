from django.db import models

# Create your models here.

# Author model
class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name

# Post model
class Post(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title