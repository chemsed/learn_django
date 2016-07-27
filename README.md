[![Gitter](https://badges.gitter.im/nagracks/learn_django.svg)](https://gitter.im/nagracks/learn_django?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

# Learn Django

Requirements
-----------

* It is using python3
* [Requirements](requirements.txt)

TODO
-----------

* [x] Start a blog app
* [x] Remove the secret_key from version control
* [x] Write basic views for the blog and the polls app
* [x] Map views to urls
* [ ] Setup the database
* [ ] Creating models
Activating models
* [ ] Create stubs for the models we'll need

Django notes
-----------

**Directory structure of project**

```
▾ blogging/
  ▾ blogging/
      __init__.py
      settings.py
      urls.py
      wsgi.py
    manage.py
	db.sqlite3
  ▾ blog/
      ▾ migrations/
	  	 __init__.py
      __init__.py
      admin.py
      apps.py
      models.py
	  tests.py
	  urls.py
	  views.py
  ▾ polls/
        ▾ migrations/
		   __init__.py
      __init__.py
      admin.py
      apps.py
      models.py
	  tests.py
	  urls.py
	  views.py
		
  LICENSE
  README.md
  requirements.txt
```

** Access to the website **
In the command line, make sure you are in the learn_django directory, if you haven’t already, and run the following commands:

	$ python manage.py runserver

For now, you can access to these urls:
	http://127.0.0.1:8000/blog/
	http://127.0.0.1:8000/polls/
	http://127.0.0.1:8000/admin/ (, but there is no admin profile created yet)

**Start App**

	$ python manage.py startapp polls`

**Adding the secret key**

* Create a file called `secrets.py` in the `blogging/blogging` folder
* Add a line saying `SECRET_KEY = 'paste the secret key here'`