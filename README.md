My first django admin

http://first-django-admin.readthedocs.org/en/latest/

=================

Pip freeze - lists all the things in your virtual env for use in a requirements.txt file

pip freeze > requirements.txt (makes the requirements file)

pip install -r requirements.txt (installs it all)

migrate - nerd jargon for working with the structure of the database. 

python manage.py migrate - creates the database, with django stuff by default

python manage.py startapp "new app"

models - database tables

views - what to pull out of database to present on a website


In Models.py (in the academy app), class Invite(models.Model): is where you set up the configuration of this database.

Views.py will connect with models.py to query the database and return the data to present on the website. ***CONFIRM

=================

// Settings in here override those in "Default/Preferences.sublime-settings",
// and are overridden in turn by file type specific settings.
{
	"font_size": 14,
	"draw_white_space": "all"
}

=================

get_display - will allow you to get info from the models

=================

python manage.py check - checks your work so far
