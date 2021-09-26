from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_db_sesssion():
    
    engine = create_engine('mssql+pyodbc://DESKTOP-DTMKRB0\\SQLEXPRESS/mydb?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server')

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)

    return Session
