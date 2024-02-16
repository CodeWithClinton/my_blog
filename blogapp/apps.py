from django.apps import AppConfig


class BlogappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogapp'



server {
    listen 80;
    server_name 146.190.167.129;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/clinton/my_blog;
    }
    
    
    location /media/ {
        root /home/clinton/my_blog;
    }
    

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/clinton/mysite.sock;
    }
}




# create user newuser;create database newdb;
# alter role newuser with password 'newpassword';
# grant all privileges on database newdb to newuser;
# alter database newdb owner to newuser;


# ALTER ROLE newuser SET client_encoding TO 'utf8';
# ALTER ROLE newuser SET default_transaction_isolation TO 'read committed';
# # ALTER ROLE newuser SET timezone TO 'UTC';
# cat ~/.ssh/id_rsa.pub | ssh root@146.190.167.129 "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"

# ssh -i ~/.ssh/id_rsa root@146.190.167.129
