# BCG_Backend
Case Study for Electricity Board 

Concepts used for implementation are
1. Pandas to read data from excel to load the data to DB
2. used sqlite3 DB

Normalizations considered for implentation for the sample data shared in excel are
1. For specific feilds certain data options were provided like Male and Female for gender.
2. For specific status, certain comment is added as the default and gave option for adding more details as well.
3. Consided reviewer as a different entity.
4. for address i have observed same pincode is available in different districts and state. so i made the unique together and gave option to add them fron frontend as well.

use `pip install -r requirements.txt` to install the dependenct pacakages

use `python manage.py makemigrations` to create migration files

use `python manage.py migrate` to apply migrate

use `python manage.py add_sample_data` to load the data in csv to DB

use `python manage.py runserver` to start the backend service

Please refer the collectios file for the API end points
