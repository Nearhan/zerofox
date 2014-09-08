# ReadMe for Zerofox

## Installation

- Use a virtual env or not, its up to you!! Just remember this installs Django 1.7 so be aware of that.
-  I am assuming you are using Virtural ENV Wrapper

- make zerfox ve
        
        mkvirtualenv zerfox

## steps

Clone the REPO

    git clone https://github.com/Nearhan/zerofox

CD into Repository
    
    cd zerofox
    
Then install dependencies

    pip install -r requirements.txt
    
Then migrate db

    python manage.py migrate
   
Then runserver


    python manage.py runserver
    
Now in a browser checkout:

    http://127.0.0.1:8000/
    
    
Enjoy!!
   
    