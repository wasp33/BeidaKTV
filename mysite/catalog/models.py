from django.db import models

# Create your models here.
class Singer(models.Model):
    name = models.CharField(max_length=30,blank=True)
    def __str__(self):
        return self.name

class Song(models.Model):
    title =  models.CharField(max_length=24)
    lang = models.CharField(max_length=10,default="國語")
    scode = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    singer = models.ForeignKey(
        Singer,
        related_name='songs',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
