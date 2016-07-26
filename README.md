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
    manage.py*
  LICENSE
  README.md
```

**Start App**

`python manage.py startapp polls`

**Adding the secret key**

* Create a file called `secrets.py` in the `blogging/blogging` folder
* Add a line saying `SECRET_KEY = 'paste the secret key here'`
