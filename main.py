import uvicorn

from application import Base_Model
from application.factory import create_app
from application.database.connection import engine
from application.utils import default_table

app = create_app()

# create database tables.
Base_Model.metadata.create_all(bind=engine)

# create all available schemas to db
from application.models import *

# create default tables
default_table.run()

if __name__ == "__main__":
    # start server
    uvicorn.run('main:app', host='localhost', port=5001, reload=True)
