
import json

from fastapi import (
    APIRouter,
    Header,
    Request,
    Response
)

from sqlalchemy import (
    create_engine,
    desc, 
    text,
)
from sqlalchemy.orm import sessionmaker

from fastapi.exceptions import HTTPException
from starlette.responses import JSONResponse


from src.models import SensorModel

# from src.utils.helpers import (
#     get_db_sesssion
#    )
from src.utils.generators.sql_db_models import Sensor, SensorHistory


engine = create_engine('mssql+pyodbc://DESKTOP-DTMKRB0\\SQLEXPRESS/SensyrtechStage2?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server',
pool_size=10000, max_overflow=0
)

DB_SESSION = sessionmaker(bind=engine)


router = APIRouter(
    prefix="/iot-api",
    tags=["iot-api"],
    responses={404: {"description": "Not found"}},
)


# @router.options("")
# def get_user_options(response: Response):
#     response.headers['Access-Control-Allow-Origin'] = json.dumps(
#         'null')
#     response.headers['Access-Control-Allow-Headers'] = json.dumps(
#         ['Content-Type', 'Authorization', 'Accept'])
#     response.headers['Access-Control-Allow-Methods'] = json.dumps(
#         ['GET', 'POST', 'DELETE', 'OPTIONS'])



@router.post("/process")
def process(request: Request, model: SensorModel):
    try:
        # db = DB_SESSION()

        # sensor = db.query(
        #    Sensor.DataTypeID,
        #    Sensor.CustomEquation,
        #    Sensor.FrequencyNumber,
        #    Sensor.SensorHardwareTypeId,
        #    Sensor.GatewayID,
        #    Sensor.MachineID,
        #    Sensor.OnMuteNotification).filter(
        #         Sensor.SensorID == str(model.sensorId)
        # ).first()

        # last_sensor_history = db.query(
        #    SensorHistory.DateTime,
        #    SensorHistory.SensorStatusID,
        #    SensorHistory.TimeElapsed,
        #    SensorHistory.Value).filter(
        #         SensorHistory.SensorID == str(model.sensorId)
        # ).order_by(desc(SensorHistory.DateTime)).first()



        sensor_status = None
        # sensor_status = db.execute('spGetSensorMachineStates ?, ?', [model.sensorId, str(model.voltage)])
        with engine.begin() as conn:
            sensor_status = conn.execute("exec dbo.spGetSensorMachineStates 'HS123', 80")
            for row in sensor_status:
                breakpoint()
                print("SensorID:", row)

        # result = db.execute("exec dbo.spGetSensorMachineStates 'HS123', 80")
        # data = [dict(r) for r in result]

        # raw_conn = db.connection().engine.raw_connection()
        # cur = raw_conn.cursor()
        # cur.execute("exec dbo.spGetSensorMachineStates 'HS123', 80")
        # breakpoint()
        # cur.nextset()
        # row = cur.fetchone()
        # process_id = row[0]
        # for result in cur.stored_results():
        #     print(result.fetchall())

        # res = db.execute('SELECT TOP 2 * FROM Sensor')
        # for r in res:
        #     breakpoint()
        #     print(r[0]) # Access by positional index
        #     print(r['Id']) # Access by column name as a string
        #     r_dict = dict(r.items()) # convert to dict keyed by column names

        # with engine.connect() as connection:
        #     # result = connection.execute(text("declare @ss table (id int, msid int, ssid int) insert into @ss EXEC dbo.spGetSensorMachineStates 'HS123', 80 select * from @ss"))
        #     result = connection.execute(text("EXEC dbo.spGetSensorMachineStates 'HS123', 80"))
        #     breakpoint()
        #     for row in result:
        #         breakpoint()
        #         print("SensorID:", row)

        # connection = engine.connect()
        # result = connection.execute(text("EXEC dbo.spGetSensorMachineStates 'HS123', 80"))
        # breakpoint()
        # for row in result:
        #     breakpoint()
        #     print("SensorID:", row)


        breakpoint()
        return JSONResponse(status_code=200, content='ok')
    except Exception as e:
        
        print(str(e))
        return JSONResponse(status_code=500, content=str(e))
