from django.db import models

# The blog will have posts and comments.
# A relationship is defined with the foreignKey method. Then, 
# many comments can be related to a blog post. 
class Post(models.Model):
	post_text = models.CharField(max_length=40000)
	pub_date = models.DateTimeField("date published")
	like = models.IntegerField(default=0)
	
class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	comment_text = models.CharField(max_length=10000)
	pub_date = models.DateTimeField("date published")