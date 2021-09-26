# coding: utf-8
from sqlalchemy import BigInteger, Boolean, Column, DECIMAL, DateTime, ForeignKey, Integer, String, Table, Time, Unicode, text
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Sensor(Base):
    __tablename__ = 'Sensor'

    SensorID = Column(String(150, 'SQL_Latin1_General_CP1_CI_AS'), primary_key=True)
    SensorName = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    MachineID = Column(Integer)
    SensorTypeID = Column(Integer)
    FrequencyNumber = Column(Integer)
    CriticalMin = Column(DECIMAL(18, 2))
    CriticalMax = Column(DECIMAL(18, 2))
    WarningMin = Column(DECIMAL(18, 2))
    WarningMax = Column(DECIMAL(18, 2))
    DataTypeID = Column(Integer)
    CustomEquation = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    SleepStart = Column(Time)
    SleepEnd = Column(Time)
    DigitalAlarm = Column(Boolean)
    DateCreated = Column(DateTime)
    DigitalLowMin = Column(DECIMAL(18, 0))
    DigitalLowMax = Column(DECIMAL(18, 0))
    DigitalHighMin = Column(DECIMAL(18, 0))
    DigitalHighMax = Column(DECIMAL(18, 0))
    DateModified = Column(DateTime)
    LastModifiedBy = Column(Integer)
    SensorTemplateID = Column(Integer)
    VoltageCriticalMin = Column(DECIMAL(18, 2))
    VoltageCriticalMax = Column(DECIMAL(18, 2))
    VoltageWarningMin = Column(DECIMAL(18, 2))
    VoltageWarningMax = Column(DECIMAL(18, 2))
    CriticalityTypeId = Column(Integer)
    ComingUnitId = Column(Integer)
    Description = Column(String(500, 'SQL_Latin1_General_CP1_CI_AS'))
    SensorTypeUnitId = Column(Integer)
    CompanyId = Column(Integer)
    SensorBlobURl = Column(Unicode)
    CreatedBy = Column(UNIQUEIDENTIFIER)
    MachineLocationId = Column(Integer)
    FrequencyNumberUnit = Column(Integer)
    IsActive = Column(Boolean)
    InactiveDate = Column(DateTime)
    PortNumber = Column(Integer)
    NotificationTemplateId = Column(Integer)
    CriticalMinState = Column(Integer)
    CriticalMaxState = Column(Integer)
    WarningMinState = Column(Integer)
    WarningMaxState = Column(Integer)
    HighActivation = Column(DECIMAL(18, 2))
    BinaryStateId = Column(Integer)
    OnStateId = Column(Integer)
    OffStateId = Column(Integer)
    ReverseEquation = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    SensorHardwareTypeId = Column(Integer)
    IsSensyrtechProvidedSensor = Column(Boolean)
    GatewayID = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    MinFrequency = Column(Integer)
    MaxFrequency = Column(Integer)
    OnMuteNotification = Column(Boolean, nullable=False)
    OffMuteNotification = Column(Boolean, nullable=False)
    Battery = Column(Integer)
    Signal = Column(Integer)
    OnAlarm = Column(Boolean)
    OffAlarm = Column(Boolean)


class SensorHistory(Base):
    __tablename__ = 'SensorHistory'

    SensorHistoryID = Column(Integer, primary_key=True)
    SensorID = Column(String(150, 'SQL_Latin1_General_CP1_CI_AS'))
    Voltage = Column(DECIMAL(9, 2))
    Value = Column(DECIMAL(18, 2))
    SensorStatusID = Column(Integer)
    DateTime = Column(DateTime)
    AVG = Column(DECIMAL(18, 2))
    MIN = Column(DECIMAL(18, 2))
    MAX = Column(DECIMAL(18, 2))
    TimeElapsed = Column(Integer, nullable=False, server_default=text("((0))"))
    OriginalMachineStateId = Column(Integer)
    IsDefaultEntry = Column(Boolean, nullable=False, server_default=text("((0))"))
    ReportId = Column(Integer)
    CurrentMachineStateId = Column(Integer)


class Gateway(Base):
    __tablename__ = 'Gateway'

    GatewayID = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'), primary_key=True)
    VariantID = Column(Integer, nullable=False)
    GatewayName = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    DateCreated = Column(DateTime, nullable=False)
    BranchID = Column(Integer)
    Signal = Column(Integer)
    Battery = Column(Integer)
    GatewayTypeId = Column(Integer)
    IsActive = Column(Boolean, nullable=False, server_default=text("((1))"))
    LastModifiedBy = Column(Integer)
    DateModified = Column(DateTime)
    CompanyId = Column(Integer)
    CreatedBy = Column(UNIQUEIDENTIFIER)
    ICCID = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    IsDirectGateway = Column(Boolean, nullable=False, server_default=text("((0))"))


class Machine(Base):
    __tablename__ = 'Machine'

    MachineID = Column(Integer, primary_key=True)
    MachineName = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    SectorId = Column(Integer)
    Description = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'))
    BranchID = Column(Integer)
    DateModified = Column(DateTime)
    DateCreated = Column(DateTime, nullable=False)
    CompanyId = Column(Integer)
    MachineBlobURl = Column(Unicode)
    LastModifiedBy = Column(UNIQUEIDENTIFIER)
    CreatedBy = Column(UNIQUEIDENTIFIER, nullable=False)
    LocationName = Column(String(225, 'SQL_Latin1_General_CP1_CI_AS'))
    MachineStateId = Column(Integer)
    SN = Column(Unicode(300))


class MachineStateHistory(Base):
    __tablename__ = 'MachineStateHistory'

    MachineStateHistoryId = Column(Integer, primary_key=True)
    MachineId = Column(Integer, nullable=False)
    MachineStateId = Column(Integer, nullable=False)
    StartDate = Column(DateTime, nullable=False)
    EndDate = Column(DateTime)
    DateCreated = Column(DateTime, nullable=False)
    CreatedBy = Column(UNIQUEIDENTIFIER, nullable=False)
    ModifyDate = Column(DateTime)
    ModifyBy = Column(UNIQUEIDENTIFIER)
    TriggerBySensorId = Column(Unicode(250))