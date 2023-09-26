# Blogmate
 A simple  Blogging app with Flask

## Overview
  Blogmate is a blogging app with flask with password encryption, user authentication and supposedly nice styling 😁 ***(..joking about that)***

> The modules used were `flask`,  `flask-bcrypt`, `flask-login`, `flask-wtf` and `flask-sqlalchemy`

>They can be installed as follows
> ### Flask
> ```python
> pip install flask 
> ```
> ### Flask-SQLalchemy
> ```python
> pip install flask-sqlalchemy
> ```
> ### Flask-Bcrypt
> ```python
> pip install flask-bcrypt 
> ```
> ### Flask-Login
> ```python
> pip install flask-login
> ```
> ### Flask-WTF
> ```python
> pip install flask-wtf 
> ```
> ```python
> pip install email-validator
> ```

### styling was done via Bootstrap css and js
> Other modules such as `time` modules are used as well

> The directory struture is as follows *(it is a lot)*
```
│   .gitattributes
│   README.md
│
└───Blogmate
    │   dba.py
    │   run.py
    │
    ├───blog
    │   │   forms.py -> Containing all form instances
    │   │   models.py -> containing all database instances
    │   │   routes.py -> containing all routes (views)
    │   │   utils.py -> all utilities such as placeholder and datetime
    │   │   __init__.py
    │   │
    │   ├───static
    │   │   ├───css
    │   │   │       .DS_Store
    │   │   │       animate.min.css
    │   │   │       bootstrap-grid.css
    │   │   │       bootstrap-grid.css.map
    │   │   │       bootstrap-grid.min.css
    │   │   │       bootstrap-grid.min.css.map
    │   │   │       bootstrap-reboot.css
    │   │   │       bootstrap-reboot.css.map
    │   │   │       bootstrap-reboot.min.css
    │   │   │       bootstrap-reboot.min.css.map
    │   │   │       bootstrap.css
    │   │   │       bootstrap.css.map
    │   │   │       bootstrap.min.css
    │   │   │       bootstrap.min.css.map
    │   │   │       default-skin.css
    │   │   │       font-awesome.min.css
    │   │   │       icomoon.css
    │   │   │       jquery-ui.css
    │   │   │       jquery.fancybox.min.css
    │   │   │       jquery.mCustomScrollbar.min.css
    │   │   │       meanmenu.css
    │   │   │       nice-select.css
    │   │   │       normalize.css
    │   │   │       owl.carousel.min.css
    │   │   │       responsive.css
    │   │   │       slick.css
    │   │   │       style.css
    │   │   │
    │   │   ├───fonts
    │   │   ├───images
    │   │   │       about-img.png
    │   │   │       banner-bg.png
    │   │   │       banner-img.png
    │   │   │       call-icon.png
    │   │   │       contact-img.png
    │   │   │       fb-icon-1.png
    │   │   │       fb-icon.png
    │   │   │       footer-logo.png
    │   │   │       img-1.png
    │   │   │       img-10.png
    │   │   │       img-2.png
    │   │   │       img-3.png
    │   │   │       img-4.png
    │   │   │       img-5.png
    │   │   │       img-6.png
    │   │   │       img-7.png
    │   │   │       img-8.png
    │   │   │       img-9.png
    │   │   │       instagram-icon-1.png
    │   │   │       instagram-icon.png
    │   │   │       like-icon.png
    │   │   │       linkedin-icon-1.png
    │   │   │       logo.png
    │   │   │       mail-icon.png
    │   │   │       search-icon.png
    │   │   │       twitter-icon-1.png
    │   │   │       twitter-icon.png
    │   │   │
    │   │   └───js
    │   │           .DS_Store
    │   │           bootstrap.bundle.js
    │   │           bootstrap.bundle.js.map
    │   │           bootstrap.bundle.min.js
    │   │           bootstrap.bundle.min.js.map
    │   │           bootstrap.js
    │   │           bootstrap.js.map
    │   │           bootstrap.min.js
    │   │           bootstrap.min.js.map
    │   │           custom.js
    │   │           jquery-3.0.0.min.js
    │   │           jquery.mCustomScrollbar.concat.min.js
    │   │           jquery.min.js
    │   │           jquery.validate.js
    │   │           modernizer.js
    │   │           plugin.js
    │   │           popper.min.js
    │   │           slider-setting.js
    │   │
    │   ├───templates
    │   │       about.html
    │   │       allblogs.html
    │   │       base.html
    │   │       contact.html
    │   │       createblog.html
    │   │       features.html
    │   │       index.html
    │   │       login.html
    │   │       signup.html
    │   │       viewblog.html
    │   │
    │   └───__pycache__
    │           forms.cpython-310.pyc
    │           models.cpython-310.pyc
    │           routes.cpython-310.pyc
    │           utils.cpython-310.pyc
    │           __init__.cpython-310.pyc
    │
    └───instance
            blog.db -> database of the website
```

### To run open the [`run.py`](Blogmate/run.py) file in the Blogmate directory

### Enjoy!!!