# Project "StudyMore"
An example of the web site built on Django 1.9
Demonstrates a system where teacher creates a courses wich can be attended by students

##Install
1. Make sure you have Pyython 3.4.3 and DJango 1.9 installed
2. Download and extract zip repo, or use git clone. I recommend you to use PyCharm to manage the project. You will need a settings.py file for it.
3. Navigate to the project folder and open terminal
4. Run <pre>python manage.py makemigrations</pre> 
5. Then run <pre>python manage.py migrate</pre> to commit models to your DB. Note, Django uses sqlLite for default. I prefer MySQL. You can connect it in file settings.py
6. Run <pre>python manage.py createsuperuser --username [username] --email [anyemail]</pre>
7. The type password twice. This will be your superuser. You will be able to access /admin/ with it
8. Run the project. If you did everything ok, you will get the webpage like this

![alt tag](https://raw.github.com/NoxCaos/django_elective_courses/master/screenshot.png)