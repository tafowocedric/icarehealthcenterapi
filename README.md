# icarehealthcenterapi

Backend Source Code for the Patient And Doctor Booking System (ICAREHEALTHCENTER).

- Language: Python 3.8+
- Framework: FastAPI

## Installation Requirements.
 - Python 3.8+
 
 ## Create the virtual environment
    virtualenv --python=/usr/bin/python3.8 venv
    source venv/bin/activate 
    pip install -r requirements.txt

## Database
    [MySQL](https://dev.mysql.com/downloads)


## Configurations
create a config.ini file using the config_template.ini file and update the information according to your system.

    cp -a config.ini.template config.ini

## Starting the application.
    python main.py 