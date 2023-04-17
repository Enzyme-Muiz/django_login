create venv environment:
python -m venv venv
venv\Scripts\activate.bat
pip install Django


















Create File => .env

Cut this from settings.py =>

SECRET_KEY = '-----your secret key-----'

Paste in .env

Write this in settings.py =>

from decouple import config

SECRET_KEY = config("SECRET_KEY")

Write this in terminal or cmd =>

pip install python-decouple

Then write this in terminal or cmd =>

pip freeze > requirements.txt

Go in cPanel and upload File .env





how to use it:
from the directory where this readme.txt file is,
run "python manage.py runserver"
