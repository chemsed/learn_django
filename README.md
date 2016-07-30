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
* [x] Setup the database
* [x] Creating models
* [x] Activating models
* [ ] Create stubs for the models we'll need
* [ ] Create an admin user
* [ ] Make the blog app modifiable in the admin

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
		 0001_initial.py
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

 Access to the website 
-----------

**Adding the secret key**

* Create a file called `secrets.py` in the `blogging/blogging` folder
* Add a line saying `SECRET_KEY = 'paste the secret key here'`

**Run website from the terminal**

In the command line, make sure you are in the learn_django directory, if you haven’t already, and run the following commands:

	$ python manage.py runserver

**Enter the urls in your browser**

For now, you can access to these urls:
* http://127.0.0.1:8000/blog/
* http://127.0.0.1:8000/polls/
* http://127.0.0.1:8000/admin/ (but there is no admin profile created yet)

 The making of the website
-----------

The way we create our website is by following the steps specified in the django tutorial as close as possible (https://docs.djangoproject.com/en/1.9/intro/tutorial01/)

**Creating a project**

The website has a urls for each pages (the table of contents), a view (what is shown on the webpage) and models (the database layout) and a database (wish has all the data for the website). The websites can be make into small parts (applications). For now, the website project was created with the command in the command line:
	$ django-admin startproject blogging

It created a blogging directory in the learn_django directory.

**Creating the apps**

Then, the blog and the polls apps were created with theses commands:
	$ python manage.py startapp polls
	$ python manage.py startapp blog

It created the blog and polls directory in the blogging directory.

**Write views**

Pages were created by modifying views.py in each directory. Then, access to the pages were created by modifying all the urls.py files in the project directory so the pages are mapped to an url. 

**Database**

* The file models.py for the blog app was changed in purpose to set up the database layout: The kind of data that we want for the website was specified.
* Run `python manage.py makemigrations blog` to create migrations for those changes

Output: 
```
Migrations for 'blog':
  0001_initial.py:
    - Create model Comment
    - Create model Post
    - Add field post to comment
```
* Run `python manage.py migrate` to apply those changes to the database.

Output: 
```
Operations to perform:
  Apply all migrations: blog, admin, sessions, contenttypes, auth
Running migrations:
  Rendering model states... DONE
  Applying blog.0001_initial... OK
```