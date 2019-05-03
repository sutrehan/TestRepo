from django.db import models

# Create your models here.

class Author(models.Model):
    author_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.author_name

class Post(models.Model):
    post_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_date = models.DateField(auto_now_add=True) 
    post_content = models.TextField()

    def __str__(self):
        return self.post_content[:50] + "..."
