import json

from fastapi import (
    APIRouter,
    Header,
    Request,
    Response
)
from datetime import datetime
from sqlalchemy import (
    create_engine,
    desc, 
    text,
)
from sqlalchemy.orm import sessionmaker

from fastapi.exceptions import HTTPException
from sqlalchemy.sql.sqltypes import DateTime
from starlette.responses import JSONResponse


from src.models import (
    SensorModel, 
    SensorHistory,
    MachineStateHistory,
    Gateway,
    Machine,
    Sensor,
)

# from src.utils.helpers import (
#     get_db_sesssion
#    )



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
        db = DB_SESSION()

        sensor_detail = db.query(
           Sensor.SensorID,
           Sensor.DataTypeID,
           Sensor.CustomEquation,
           Sensor.FrequencyNumber,
           Sensor.SensorHardwareTypeId,
           Sensor.GatewayID,
           Sensor.MachineID,
           Sensor.OnMuteNotification).filter(
                Sensor.SensorID == str(model.sensorId)
        ).first()

        last_sensor_history = db.query(
           SensorHistory.DateTime,
           SensorHistory.SensorStatusID,
           SensorHistory.TimeElapsed,
           SensorHistory.Value).filter(
                SensorHistory.SensorID == str(model.sensorId)
        ).order_by(desc(SensorHistory.DateTime)).first()
        sensor_status = None
        with engine.begin() as conn:
            rows = conn.execute(f"EXEC dbo.spGetSensorMachineStates {model.sensorId}, {model.voltage}")
            for row in rows:
                sensor_status = {
                    'id': row[0],
                    'machine_state_id': row[1],
                    'sensor_state_id': row[2]
                }
                break

        if True:
            found_gateway = db.query(Gateway).filter(
                Gateway.GatewayID == sensor_detail.GatewayID
            ).first()
            existing_machine_status = db.query(Machine).filter(
                Machine.MachineID == sensor_detail.MachineID
            ).first()
            
            if found_gateway and found_gateway.IsDirectGateway:
                update_existing_sensor_sql = f"UPDATE Sensor SET Battery={model.battery}, Signal={model.signal} WHERE SensorID='{sensor_detail[0]}'"
                with engine.begin() as conn:
                    rows = conn.execute(update_existing_sensor_sql)

                state = None
                with engine.begin() as conn:
                    rows = conn.execute(f"EXEC dbo.spUpdateMachineState '{model.sensorId}', 35, {model.voltage}, NULL")
                    for row in rows:
                        state = {
                            'machine_id': row[0],
                            'machine_name': row[1],
                            'machine_state_id': row[2],
                            'sensor_status_id': row[3],
                            'is_incident_occur': row[4],
                            'is_incident_resolve': row[5],
                            'original_machine_state_id': row[6],
                            'report_id': row[7],
                        }
                        break
                max_sensor_history_id = db.execute("select max(SensorHistoryID) from SensorHistory").first()[0]
                max_sensor_history_id = 0 if max_sensor_history_id == None else max_sensor_history_id
                new_sensor_history = SensorHistory(
                    SensorHistoryID = 0,
                    AVG = 1,
                    DateTime = datetime.now(),
                    MAX = 10,
                    MIN = 1,
                    SensorID  = model.sensorId,
                    SensorStatusID = state['sensor_status_id'] if state else None,
                    Value = model.voltage,
                    Voltage = model.voltage,
                    OriginalMachineStateId = state['original_machine_state_id'] if state else None,
                    CurrentMachineStateId =  state['sensor_status_id'] if state else None,
                    TimeElapsed = 2,
                    ReportId = state['report_id'] if state else None,
                )
                # db.add(new_sensor_history)
                # db.commit()

                if True:
                    last_state_history = db.query(SensorHistory).filter(
                        MachineStateHistory.MachineId == state['machine_id']
                    ).order_by(desc(MachineStateHistory.DateCreated)).first()

                    if last_sensor_history:
                        update_existing_sensor_sql = f"UPDATE MachineStateHistory SET EndDate=CONVERT(DATETIME, '2021-09-26 10:47:36.827'), ModifyDate=CONVERT(DATETIME, '2021-09-26 10:47:36.827'), ModifyBy=NULL WHERE MachineId='{state['machine_id']}'"
                        with engine.begin() as conn:
                            rows = conn.execute(update_existing_sensor_sql)
                    new_machine_state_history = MachineStateHistory(
                        MachineId = state['machine_id'],
                        MachineStateId = int(state['machine_state_id']),
                        StartDate = datetime.now(),
                        CreatedBy = None,
                        DateCreated = datetime.now(),
                        TriggerBySensorId = model.sensorId
                    )
                    # db.add(new_machine_state_history)
                    # db.commit()

                updated_sensor_details = None
                with engine.begin() as conn:
                    rows = conn.execute(f"EXEC dbo.spGetSensorDetail '{model.sensorId}'")
                    for row in rows:
                       updated_sensor_details = row
                       break


        return JSONResponse(status_code=200, content={
            "SensorID": updated_sensor_details[0],
            "Status": updated_sensor_details[10]
        })
    except Exception as e:
        
        print(str(e))
        return JSONResponse(status_code=500, content=str(e))
