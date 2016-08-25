from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.utils import timezone

# The blog will have posts and comments.
# A relationship is defined with the foreignKey method. Then,
# many comments can be related to a blog post.


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(default=None)
    pub_date = models.DateTimeField("date published")
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.TextField()
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.comment_text
