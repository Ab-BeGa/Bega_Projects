from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Twit(models.Model):
    content = models.TextField("Контент")
    postDate = models.DateTimeField("Дата публикации", default=datetime.now)
    twitImage = models.CharField("Ссылка на изображение", max_length=500, null=True, blank=True)
    userPost = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", default="")

    def __str__(self):
        return f"Пост пользователя #{self.pk}"

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"



class FavoritePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Twit', on_delete=models.CASCADE)