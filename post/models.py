from django.db import models
from django.contrib.auth.models import User
# Create your models here


class Post(models.Model):
    title = models.CharField(("Post Başlığı"), max_length=50, default="")
    endPoint = models.SlugField(("URL"), default="")
    message = models.TextField(("Mesaj"), max_length=350, default="")
    image = models.FileField(("Post Resmi"), upload_to="banner", max_length=100, null=True, blank=True)
    createdAt = models.DateTimeField(("Oluşturulma Tarihi"), auto_now=True)
    author = models.ForeignKey(User, verbose_name=("Postu Oluşturan"), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.endPoint

    def uniqueId(self):
        return self.id

    




class Comments(models.Model):
    post = models.ForeignKey(Post, verbose_name=("Gönderi"), related_name="yorumlar", on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name=("Yorum Yapan"), on_delete=models.CASCADE)
    message = models.TextField(("Mesaj"))
    createdAt = models.DateTimeField(("Tarih"), auto_now=True)

    class Meta:
     # her class oluştuğunda bunlara birtane primary key atanır.
     ordering=['-pk']


    def __str__(self) -> str:
        return "{user} {post} gönderisine yorum yaptı.".format(user=self.author, post=self.post.title)

    def redirectPage(self):
        return self.post.endPoint
