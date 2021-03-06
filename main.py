import uvicorn

from application import Base_Model
from application.database.connection import engine
from application.factory import create_app

app = create_app()

# create database tables.
Base_Model.metadata.create_all(bind=engine)

if __name__=="__main__":
    # start server
    uvicorn.run('main:app', host='localhost', port=5001, reload=True)
