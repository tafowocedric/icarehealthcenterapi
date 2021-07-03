from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autoflush=True, autocommit=True, bind=engine)

# session hook
def session_hook(func):
    """
        hook opens a database session do a session_hook(read or write) and closes the connection after the run()
        func: function that communicates with the database (e.g fun(*args, db: Session))
        returns;
        data: The return from func
        error: in case of an error in hook
    """
    def run(*args, **kwargs):
        global db

        try:
            db = SessionLocal()

            data = func(db, *args, **kwargs)
            return data

        except Exception as e:
            raise (Exception(e))

        finally:
            db.close()

    return run
