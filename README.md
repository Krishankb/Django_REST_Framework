# Django_REST_Framework
Its a Django project. In this we can create,update,delete,view,upload an image, Resize the image to 140px * 140 px.
#
#
# Instruction to Run
1. Libararies used (django-imagekit,djangorestframework,Mysql)

2. Create Migrations : python manage.py makemigrations

3. Migrate : python manage.py migrate

4. create of superuser : python manage.py createsuperuser 

5.run on the saerver : python manage.py runserver 

6. To create : localhost/api/product-create
   To 'List': 'api/product-list/',
   To  'Detail View': 'api/product-detail/<int:id>/',
   To  'Update': 'api/product-update/<int:id>/',
   To  'Delete': 'api/product-detail/<int:id>/'
