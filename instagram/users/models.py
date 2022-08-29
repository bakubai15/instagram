from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50, verbose_name="Имя пользователя")
    name = models.CharField(max_length=50, verbose_name="Имя")
    surname = models.CharField(max_length=50, verbose_name="Фамилия")
    data_of_birth = models.DateTimeField( verbose_name="Дата рождения")
    profile_image = models.ImageField(verbose_name="Фотография профиля")
    description = models.CharField(max_length=100, verbose_name="Описание")
    info_link = models.CharField(max_length=150, verbose_name="Ссылка на соц сеть", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"