from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=150)
    title_tag = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author) #this allows us to the admin page to see the title of a blog post and the author

    def get_absolute_url(self):
        #return reverse('articles_detail', args=(str(self.id)))
        return reverse('home')                             
    