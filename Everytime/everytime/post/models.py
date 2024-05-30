from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    anonymity = models.BooleanField(default = True) # 익명

    def __str__(self):
        return self.title