from email.mime import image
from tabnanny import verbose
from tkinter import CASCADE
from turtle import title
from django.db import models
from users.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=55, verbose_name="Заголовок поста")
    description = models.CharField(max_length=300, verbose_name="Описание")
    image = models.ImageField(upload_to = 'post_image/')
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_user")

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "Пост"
        verbose_name_plural = "Посты"