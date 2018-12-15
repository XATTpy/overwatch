from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Hero(models.Model):
    class Meta():
        db_table = 'Hero'

    Hero_url = models.URLField()
    Hero_name = models.CharField(max_length=25)
    Hero_bg = models.URLField()

    def __str__(self):
        return self.Hero_name


class Video(models.Model):
    class Meta():
        db_table = "Video"

    Video_url = models.CharField(max_length=200)
    Video_name = models.CharField(max_length=200)
    Video_dis = models.TextField()
    Video_date = models.DateTimeField(auto_now_add=True)
    Video_likes = models.IntegerField(default=0)


    def __str__(self):
        return self.Video_name

class Comment(models.Model):
    class Meta():
        db_table = "Comment"

    Comment_text = models.TextField(verbose_name="Введите текст")
    Comment_data = models.DateTimeField(auto_now_add=True)
    Comment_User = models.ForeignKey(User, on_delete=models.CASCADE)
    Comment_Video = models.ForeignKey(Video, on_delete=models.CASCADE)
    Comment_likes = models.IntegerField(default=0)
# Create your models here.