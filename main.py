import uvicorn
from application.factory import create_app
from application.model.base_model import Base
from application.database.connection import engine

app = create_app()

# create database tables.
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    # start server
    uvicorn.run('main:app', host='localhost', port=5001, reload=True)
