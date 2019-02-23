# Ecolibrium Assessment

Timezone based Task Execution
A configuration where users can setup the time when they want to perform a
particular task.

Source Code:
------------

`<https://github.com/BHushanRathod/ecolibrium-assessment>`_


Installation and Usage
======================

Download the souce code::
       
    $ git clone https://github.com/BHushanRathod/ecolibrium-assessment.git
    $ cd ecolibrium-assessment
   
Activate the Virtual Environment::

    source ~/path/to/ve/bin/activate

Install the Dependencies::

    pip install -r requirements.txt

Run Migrations::
    
    ./manage.py makemigrations
    ./manage.py migrate

Upload the seed data::

    ./manage.py loaddata seed_values.json
    
Create new superuser::
    
    ./manage.py createsuperuser

Run server::
    
    ./manage.py runserver <port>
    
Run TestCases::

    python manage.py test
    
Hit the server::

    https://localhost:<port>/admin
    
* Steps to follow:
    
    * In admin panel create new users. Default <U1, U2, bhushan>.
    * Add few task type in Task Type. default <Email, SMS, Call>
    * Add Country Names according. Default <USA, India>
    * Create new Task execution program in Execution List.
    * On task creation it will show you whether task is getting executed or not.
    * If the task is within time frame it will show the output as::
        ```sh
        Status: True
        ```
    * If the added task does not matches with time contrains, it will show the output as::
        ```sh
        Status: False | Next Execution at: <Date>
        ```
    * Day field in optional while adding program for execution. if day field added then output will be as::
        ```sh
        Status: False | Next Execution at: <Date> <Day>
  