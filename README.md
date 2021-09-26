# Steps to run on Windows OS
- Download and install Python 3.7.11 from https://www.python.org/downloads/
- Clone Repo -> main branch
- Restore MSSQL Database Backup
- Now change MSSQL server connection string in the following file
``` IOT-Web-Services/src/routers/sensor.py  ```
- Go to IOT-WEB-SERVICES folder and install dependencies by running following command
``` pip install -r requirements.txt ```
- Now execute following command
``` python -m uvicorn src.app:app --reload ```
- API will be available at http://localhost:8000/healthcheck
