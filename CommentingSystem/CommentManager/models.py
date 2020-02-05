from django.db import models


class Pages(models.Model):
    # url = models.URLField()
    # text = models.CharField(max_length=10)
    # page_id = models.IntegerField(primary_key=True)
    pass


class Post(models.Model):
    # page = models.ForeignKey(Pages,on_delete=models.CASCADE)
    post_id = models.IntegerField(primary_key=True)

    pass


class Comment(models.Model):

    author = models.CharField(max_length=50,null=False)
    text = models.TextField(max_length=1000,null=False)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(auto_now_add=True)

    def me(self):
        pass


class WebSite(models.Model):
    pass


class User(models.Model):
    pass
