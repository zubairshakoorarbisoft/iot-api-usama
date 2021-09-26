# coding: utf-8
from sqlalchemy import Boolean, Column, DECIMAL, DateTime, ForeignKey, Integer, String, Time, Unicode
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


class Order(Base):
    __tablename__ = 'Orders'

    OrderID = Column(Integer, primary_key=True)
    OrderNumber = Column(Integer, nullable=False)
    SensorID = Column(ForeignKey('Sensor.SensorID'))

    Sensor = relationship('Sensor')
