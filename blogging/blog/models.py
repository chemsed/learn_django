from django.db import models

# The blog will have posts and comments.
# A relationship is defined with the foreignKey method. Then,
# many comments can be related to a blog post.


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField("date published")
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.body


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.TextField()
    pub_date = models.DateTimeField("date published")
        def __str__(self):
        return self.comment_text