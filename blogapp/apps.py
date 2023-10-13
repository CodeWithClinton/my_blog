from django.apps import AppConfig


class BlogappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogapp'


# create user newuser;create database newdb;
# alter role newuser with password 'newpassword';
# grant all privileges on database newdb to newuser;
# alter database newdb owner to newuser;


# ALTER ROLE newuser SET client_encoding TO 'utf8';
# ALTER ROLE newuser SET default_transaction_isolation TO 'read committed';
# ALTER ROLE newuser SET timezone TO 'UTC';