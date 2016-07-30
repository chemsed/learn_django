from django.db import models

# Blog post models
class Post(models.Model):
	post_text = models.CharField(max_length=40000)
	pub_date = models.DateTimeField("date published")
	like = models.IntegerField(default = 0)
	
class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	
