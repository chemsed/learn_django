**Adding and manipulating data**

> /GitHub/learn_django/blogging

`$ python manage.py shell`

Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (In                                                      tel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)

```
>>> import django
>>> django.setup()
>>> from blog.models import Post, Comment
>>> Post.objects.all()
```

[]

```
>>> from django.utils import timezone
>>> p = Post(title="Welcome to our website", body="Under construction", pub_date = timezone.now())
>>> p.save()
>>> p.id
```
1

`>>> p.title`

'Welcome to our website'

`>>> p.body`

'Under construction'

`>> p.pub_date`

datetime.datetime(2016, 8, 25, 15, 52, 15, 672130, tzinfo=\<UTC\>)

```
>>> p.title="please stand by..."
>>> p.save()
>>> Post.objects.all()
```

[\<Post: please stand by...\>]

`>>> Post.objects.filter(id=1)`

[\<Post: please stand by...\>]

`>>> Post.objects.filter(title__startswith="Please")`
 
[\<Post: please stand by...\>]

```
>>> from django.utils import timezone
>>> current_year=timezone.now().year
>>> Post.objects.get(pub_date__year=current_year)
```

\<Post: please stand by...\>

`>>> Post.objects.get(id=2)`

Traceback (most recent call last):
  ...
  
blog.models.DoesNotExist: Post matching query does not exist.

`>>> Post.objects.get(pk=1)`

\<Post: please stand by...\>

```
>>> p=Post.objects.get(pk=1)
>>> p.was_published_recently()
```

True

`>>> p.comment_set.all()`

[]

`>>> p.comment_set.create(comment_text="I can't wait", pub_date=timezone.now())`

\<Comment: I can't wait\>

```
>>> import datetime
>>> p.comment_set.create(comment_text="Cool", pub_date=timezone.now()-datetime.timedelta(days=1))
```

\<Comment: Cool\>

`>>> p.comment_set.create(comment_text="What are the topics?", pub_date=timezone.now())`

\<Comment: What are the topics?\>

```
>>> c=p.comment_set.create(comment_text="Last", pub_date=timezone.now())
>>> c.post
```

\<Post: please stand by...\>

`>>> p.comment_set.all()`

[\<Comment: I can't wait\>, \<Comment: Cool\>, \<Comment: What are the topics?\>, \<Comment: Last\>]


`>>> p.comment_set.count()`

4

`>>> Comment.objects.filter(post__pub_date__year=current_year)`

[\<Comment: I can't wait\>, \<Comment: Cool\>, \<Comment: What are the topics?\>, \<Comment: Last\>]

```
>>> c=p.comment_set.filter(comment_text__startswith="Last")
>>> c.delete()
```

(1, {'blog.Comment': 1})

`>>> exit()`

**Verify the database addition by using the python shell and django API again**

> /GitHub/learn_django/blogging

`$ python manage.py shell`

Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)

```
>>> import django
>>> django.setup()
>>> from blog.models import Post, Comment
>>> Post.objects.all()
```

[\<Post: please stand by...\>]

`>>> Comment.objects.all()`

[\<Comment: I can't wait\>, \<Comment: Cool\>, \<Comment: What are the topics?\>]

**Other commands**

`>>> Comment.objects.get(post=1)`

Traceback (most recent call last):
...
blog.models.MultipleObjectsReturned: get() returned more than one Comment -- it returned 3!

`>>> Comment.objects.filter(post__id=1)`

[\<Comment: I can't wait\>, \<Comment: Cool\>, \<Comment: What are the topics?\>]

`>>> Comment.objects.filter(post=1)`

[\<Comment: I can't wait\>, \<Comment: Cool\>, \<Comment: What are the topics?\>]