# Blog-Creator
Seperate API and Front-end MVC implementation { Two Tier }
  
  all the three major components that are typically used to build web apps:

    UI (Frontend) ===> Written in AngularJs

    APIs (Middleware) ===> Written in Django Rest Framework

    Database (Backend) ===> SQlite used for default auth models and MongoDB used for storing blog posts
    
  You need to install MongoDb to your system before u proceed
  
  In Order to run the project 
    
    just clone the Repo and change directory to servers type in
    
      pip install -r requirements.txt
      
    Now stop the running mongodb server and unzip data.tar.bz2. Then run mongo as
      
      ./mongod
    
    then create a superuser and django app as
    
      python manage.py createsuperuser
      python manage.py runserver 0.0.0.0:8000
      
    login with superuser credentials and navigate to 
    
      http://localhost:8000/posts/
      
    to see all the posts
    
  In Order to run client side app
  
    change directory to client and type-in
      
      node server.js
      
    Then navigate to
    
      http://localhost:3000/
    
    to view all posts
