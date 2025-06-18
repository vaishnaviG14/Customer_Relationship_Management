# Customer_Relationship_Management
A web application built with Django and PostgreSQL to manage customer and staff information. This app allows authenticated users to perform full CRUD operations (Create, Read, Update, Delete) on records and manage login/logout functionality.

🛠️ Technologies Used-  
Python 3  
Django Web Framework  
PostgreSQL  
Bootstrap 5  
HTML/CSS  

🚀 Features-  
User Authentication (Login/Logout)  
Add New Records (Customer or Staff)  
View Individual Record Details  
Delete Records  
Restrict access to logged-in users only  
Backed by PostgreSQL database  
Clean, responsive UI using Bootstrap  

🗃️ Setup-  
pip install virtualenv  
virtualenv virt  
virt\Scripts\activate  # Windows  
pip install django  
pip install psycopg2  
python manage.py makemigrations  
python manage.py migrate  
python manage.py createsuperuser  
python manage.py runserver  

Only users regsterd on admin (Superuser) panel can login
admin panel- http://127.0.0.1:8000/admin

to start- python manage.py runserver
![Home Page](https://github.com/vaishnaviG14/Customer_Relationship_Management/blob/main/Home.png)
