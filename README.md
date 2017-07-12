# assets-store
Assets Store created using Python 2.7/django 1.10.5

checkout git repository

git clone https://github.com/nagaraju2015git/assets-store.git

Install pre-requisistes 

pip install -r requirements.txt --no-index

On terminal, go to the checked-out directory and run below commands

  step 1 : python manage.py createsuperuser (give admin as username and admin@assetstore.com as email and password123 as password) 
  
  step 2: python manage.py runserver

From browser, goto http://127.0.0.1:8000/admin (Enter Userid as admin and password as password123 or whatever you created in step 1)

On browser, goto http://127.0.0.1:8000/assets/ and see list of asset and also to create any new asset. You can use GET or PUT requests for assets

You can click on Swagger Schema, to see the API documentation

http://127.0.0.1:8000/

![Alt text](https://github.com/nagaraju2015git/assets-store/blob/master/images/img1.png?raw=true "Get")

![Alt text](https://github.com/nagaraju2015git/assets-store/blob/master/images/img2.png?raw=true "Post")

Swaager API Documentation:

![Alt text](https://github.com/nagaraju2015git/assets-store/blob/master/images/img4.png?raw=true "API documentation in swagger")

