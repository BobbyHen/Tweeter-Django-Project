# Tweeter Django Project

Tweeter is a social media project created with Django 3 and MongoDB. This project was created for a workshop series for Broward College's inTech club. This repo acts as a learning tool and as an example of what can be done with Django.
## Installation / Project Setup


#### Install pipenv
```bash
pip install pipenv
```
#### CD into the main repo directory and run the virtural environment

```bash
pipenv shell
```

#### Once in the virtural environment, install django

```bash
pipenv install django
```

#### After installing Django, make sure to install the following dependencies:

* dnspython
* djongo - The engine used to connect to a mongo database
* pillow - Used to manipulate images

```bash
pipenv install dnspython
pipenv install djongo
pipenv install pillow
```

### Setting up Mongo DB with Atlas

Go to [mongodb.com](https://www.mongodb.com/) to setup an account with Mongo atlas and use their cloud solution or run a local instance of mongo. 

## Usage

To connect to your mongo database, modify the database connection portion of your settings.py file shown below.
```python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'your db name here',
        'CLIENT': {
            'host': 'Mongo connection string here'
        }
    }
}
```
* Change the __NAME__ value to the name of your database
* Change the __host__ to your connection string

## For Deployment
Visit [djecrety.ir](https://djecrety.ir/) to generate a secret key and place it in the settings.py shown below as a string
```python
SECRET_KEY = '' # Django secret key here
```
For more info on deploying Django projects like this, visit the official Django documentation  [here](https://docs.djangoproject.com/en/3.0/howto/deployment/).